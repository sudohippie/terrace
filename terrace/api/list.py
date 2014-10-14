__author__ = 'Raghav Sidhanti'

from flask import Blueprint
from flask import request, jsonify, url_for

list_api = Blueprint('list_api', __name__)


@list_api.route('/lists', methods=['GET', 'POST'])
def all_lists():
    if request.method == 'GET':
        return jsonify({'id': 'lists', 'method': 'GET'})
    elif request.method == 'POST':
        return jsonify({'id': 'lists', 'method': 'POST'})


@list_api.route('/list/<int:list_id>', methods=['GET', 'PUT', 'DELETE'])
def list_by_id(list_id):
    if request.method == 'GET':
        return jsonify({'id': list_id, 'method': 'GET'})

    elif request.method == 'PUT':
        return jsonify({'id': list_id, 'method': 'PUT'})

    elif request.method == 'DELETE':
        return jsonify({'id': list_id, 'method': 'DELETE'})

