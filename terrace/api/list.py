__author__ = 'Raghav Sidhanti'

from flask import Blueprint
from flask import request, jsonify, url_for

api = Blueprint('api', __name__)


@api.route('/list', methods=['POST'])
def add_list():
    name = request.json.get('name')
    return jsonify({'name': name})


@api.route('/lists', methods=['GET'])
def get_lists():
    return jsonify({'url': url_for('api.get_lists')})


@api.route('/list/<int:list_id>', methods=['GET', 'PUT', 'DELETE'])
def get_list(list_id):
    if request.method == 'GET':
        return jsonify({'id': list_id, 'method': 'GET'})

    elif request.method == 'PUT':
        return jsonify({'id': list_id, 'method': 'PUT'})

    elif request.method == 'DELETE':
        return jsonify({'id': list_id, 'method': 'DELETE'})

