__author__ = 'rsidhanti'

from flask import Blueprint
from flask import request, jsonify

list_item_api = Blueprint('list_item_api', __name__)


@list_item_api.route('/list/<list_id>/items', methods=['GET', 'POST'])
def list_items(list_id):
    if request.method == 'GET':
        return jsonify({'id': list_id, 'method': 'GET'})
    elif request.method == 'POST':
        return jsonify({'id': list_id, 'method': 'POST'})


@list_item_api.route('/list/<list_id>/item/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def list_item_by_id(list_id, item_id):
    if request.method == 'GET':
        return jsonify({'list_id': list_id, 'item_id': item_id, 'method': 'GET'})

    elif request.method == 'PUT':
        return jsonify({'list_id': list_id, 'item_id': item_id, 'method': 'PUT'})

    elif request.method == 'DELETE':
        return jsonify({'list_id': list_id, 'item_id': item_id, 'method': 'DELETE'})
