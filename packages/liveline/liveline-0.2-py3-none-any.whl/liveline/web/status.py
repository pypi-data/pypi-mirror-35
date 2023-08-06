from flask import Blueprint, json


def build_status_blueprint():
    status = Blueprint('status', __name__)

    # pylint: disable=W0612
    @status.route('/health')
    def health_check():
        return json.jsonify({'health': 'ok'})

    return status