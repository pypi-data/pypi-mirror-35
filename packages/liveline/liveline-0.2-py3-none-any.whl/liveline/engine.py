import json
import copy
import logging
import os
import time
import traceback
from datetime import datetime, tzinfo
from threading import Thread, Timer
from typing import Dict, List

import arrow
import pandas as pd
import pandas_market_calendars as mcal
import pytz
import schedule
from flask import Flask

from liveline.data import LiveLineData
from liveline.model import Options, Order, OrderStatus, Stock
from liveline.order import LiveLineOrder, OrderExecutor, PoolExecutor

from liveline.web import build_status_blueprint, build_strategy_blueprint

from .context import Context, ContextDataStore


class Strategy:
    def __init__(self):
        self.logger = logging.getLogger(self.name)

    @property
    def name(self):
        pass

    @property
    def interval(self) -> int:
        """
        Interval to run this strategy in minutes.
        """
        return 5

    def run(self,
            context: Context,
            data: LiveLineData,
            order: LiveLineOrder):
        pass


class LiveLine:
    def __init__(self, data: LiveLineData, order: LiveLineOrder, context_store: ContextDataStore):
        self.logger: logging.Logger = logging.getLogger('LiveLine')
        self.data: LiveLineData = data
        self.order: LiveLineOrder = order
        self.context_store = context_store
        self.paused = True
        self.strategies: Dict[str, Strategy] = dict()

    @property
    def livelineorder(self) -> LiveLineOrder:
        return self.order

    @property
    def livelinedata(self) -> LiveLineData:
        return self.data

    @property
    def market_open_time(self) -> arrow.Arrow:
        return arrow.get(datetime(2018, 6, 1, 9, 30), 'US/Eastern')

    @property
    def market_close_time(self) -> arrow.Arrow:
        return arrow.get(datetime(2018, 6, 1, 16, 0), 'US/Eastern')

    def is_market_open_on(self, date: arrow.Arrow):
        us_east_date = date.to('US/Eastern')
        us_east_date = us_east_date.replace(hour=10, minute=1)

        nyse = mcal.get_calendar('NYSE')
        early = nyse.schedule(start_date='2018-07-01', end_date='2022-07-10')
        return nyse.open_at_time(early, pd.Timestamp(us_east_date.format('YYYY-MM-DD HH:mm'), tz='America/New_York'))

    def add_strategy(self, strategy: Strategy):
        if strategy.name in self.strategies:
            raise ValueError(
                'Strategy called %s already exist, cannot have duplicate names' % strategy.name)
        self.strategies[strategy.name] = strategy

    def get_strategies(self) -> List[Strategy]:
        return copy.copy(self.strategies)

    def __register_flask_blueprint__(self):
        status_bp = build_status_blueprint()
        self.app.register_blueprint(status_bp, url_prefix='/status')

        strategy_bp = build_strategy_blueprint(self)
        self.app.register_blueprint(strategy_bp, url_prefix='/strategy')

    def start(self, debug=False, web_server=True):
        if web_server:
            self.app = Flask(__name__)
            flask_logging_level = logging.WARNING
            # pylint: disable=E1101
            self.app.logger.setLevel(flask_logging_level)
            logging.getLogger('werkzeug').setLevel(flask_logging_level)

            # register blueprints
            self.__register_flask_blueprint__()

            # start flask thread
            port = int(os.environ['PORT']) if 'PORT' in os.environ else 8080
            flask_thread = Thread(target=self.app.run, kwargs={
                                  'port': port}, name='flask')
            self.logger.info('Flask server listening at %d ...' % port)
            flask_thread.start()

        if not debug:
            ll_thread = Thread(target=self.__schedule__,
                               name='Livelive engine')
            self.logger.info('===============================')
            self.logger.info('| LiveLine Engine has started |')
            self.logger.info('|        by Daniel Wang       |')
            self.logger.info('===============================')
            ll_thread.start()
        else:
            debug_thread = Thread(target=self.__day_start__)
            self.logger.debug('Running a debug liveline thread...')
            debug_thread.start()

    def __schedule__(self):
        local_market_open_time = self.market_open_time.to('local')
        local_market_close_time = self.market_close_time.to('local')
        engine_start_time = '%02d:%02d' % (local_market_open_time.hour,
                                           local_market_open_time.minute)
        engine_pause_time = '%02d:%02d' % (local_market_close_time.hour,
                                           local_market_close_time.minute)
        schedule.every().day.at(engine_start_time).do(self.__day_start__)
        schedule.every().day.at(engine_pause_time).do(self.__day_pause__)

        self.logger.info('Engine runs at %s everyday' % engine_start_time)
        self.logger.info('Engine pauses at %s everyday' % engine_pause_time)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def __day_start__(self):
        self.logger.info('Engine started on market open')
        self.paused = False

        for name in self.strategies:
            try:
                self.__run_strategy__(self.strategies[name])
            except Exception as e:
                self.logger.error('Error when running strategy %s' %
                                  name, exc_info=e, stack_info=True)

    def __day_pause__(self):
        self.logger.info('Engine paused on market close')
        self.paused = True

    def __run_strategy__(self, strategy: Strategy):
        if self.paused:
            return

        # schedule a timer for next run
        interval_in_seconds = 60 * strategy.interval
        timer = Timer(interval_in_seconds, self.__run_strategy__, [strategy])
        timer.start()

        # run current loop for stategy
        self.logger.info('>> Running strategy %s' % strategy.name)
        try:
            # find context from previous execution
            context = self.context_store.get_strategy_latest_context(
                strategy.name)
            if context is None:
                self.logger.debug(
                    'No previous context found for %s, create a new one' % strategy.name)
                context = Context()
            else:
                self.logger.debug(
                    'Found a previous context for %s' % strategy.name)

            # build order pool for this execution
            stock_pool: PoolExecutor = PoolExecutor[Stock]()
            options_pool: PoolExecutor = PoolExecutor[Options]()
            ll_order_pool = LiveLineOrder(stock_pool, options_pool)

            # run strategy
            strategy.run(context, self.livelinedata, ll_order_pool)

            # save context
            try:
                self.context_store.save(strategy.name, context)
                self.logger.debug('Context saved for %s' % strategy.name)
            except Exception as e:
                self.logger.error('Cannot save context for %s' % strategy.name)
                raise e

            # validate and execute orders
            for stock_order in stock_pool.pool:
                self.__place_order__(self.livelineorder.stock, stock_order)
            for options_order in options_pool.pool:
                self.__place_order__(self.livelineorder.options, options_order)
        finally:
            self.logger.info('<< Finished strategy %s' % strategy.name)

    def __place_order__(self, executor: OrderExecutor, order: Order):
        try:
            executor.place_order(order.equity, order.quantity,
                                 order.price, order.order_type)
        except Exception as e:
            self.logger.error('Failed to place order <%s>' % order)
            raise e
