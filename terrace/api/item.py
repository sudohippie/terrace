__author__ = 'Raghav Sidhanti'

from flask import Blueprint
from flask import request, jsonify, url_for

item_api = Blueprint('item_api', __name__)


@item_api.route('/items', methods=['GET', 'POST'])
def all_items():
    if request.method == 'GET':
        return jsonify({'id': 'items', 'method': 'GET'})
    elif request.method == 'POST':
        return jsonify({'id': 'items', 'method': 'POST'})

