__author__ = 'Raghav Sidhanti'

from terrace.db import dao
from flask import Blueprint
from flask import request, jsonify, url_for

list_api = Blueprint('list_api', __name__)


@list_api.route('/lists', methods=['GET', 'POST'])
def all_lists():
    if request.method == 'GET':
        lists = dao.get_all_lists()
        vals = []
        for l in lists:
            val = {'id': l.id, 'name': l.name, 'update_date': l.update_date, 'create_date': l.create_date}
            vals.append(val)

        return jsonify({'lists': vals})

    elif request.method == 'POST':
        name = request.json.get('name')
        l = dao.save_list(name)
        return jsonify({'id': l.id, 'name': l.name, 'update_date': l.update_date, 'create_date': l.create_date})


@list_api.route('/list/<int:list_id>', methods=['GET', 'PUT', 'DELETE'])
def list_by_id(list_id):
    if request.method == 'GET':
        return jsonify({'id': list_id, 'method': 'GET'})

    elif request.method == 'PUT':
        return jsonify({'id': list_id, 'method': 'PUT'})

    elif request.method == 'DELETE':
        return jsonify({'id': list_id, 'method': 'DELETE'})

