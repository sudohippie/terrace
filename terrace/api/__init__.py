__author__ = 'Raghav Sidhanti'

from terrace.api.list import api
from terrace import flask_app

flask_app.register_blueprint(api, url_prefix='/api')
