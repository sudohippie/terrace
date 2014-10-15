__author__ = 'Raghav Sidhanti'

from terrace import flask_app
from terrace.api.list import list_api
from terrace.api.item import item_api
from terrace.api.list_item import list_item_api

flask_app.register_blueprint(list_api, url_prefix='/api')
flask_app.register_blueprint(item_api, url_prefix='/api')
flask_app.register_blueprint(list_item_api, url_prefix='/api')
