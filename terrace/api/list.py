__author__ = 'Raghav Sidhanti'

from terrace.db import list_dao
from flask import Blueprint
from flask import request, jsonify
from httplib import BAD_REQUEST, NOT_FOUND, OK

list_api = Blueprint('list_api', __name__)


@list_api.route('/lists', methods=['GET', 'POST'])
def all_lists():
    results = None

    if request.method == 'GET':
        all = list_dao.get_all()
        for l in all:
            results.append(get_list_as_dict(l))

    elif request.method == 'POST':
        contents = request.json.get('lists')

        for content in contents:
            l = list_dao.save(name=content.get('name'))
            results.append(get_list_as_dict(l))

    return jsonify({'lists': results})


@list_api.route('/list/<int:list_id>', methods=['GET', 'PUT', 'DELETE'])
def list_by_id(list_id):
    result = {}
    status_code = OK

    if request.method == 'GET':
        one = list_dao.get_by_id(list_id)
        result = get_list_as_dict(one)

        if one is None:
            status_code = NOT_FOUND

    elif request.method == 'PUT':
        name = request.json.get('name')

        if name is None:
            status_code = BAD_REQUEST
        else:
            l = list_dao.update(list_id=list_id, name=name)
            result = get_list_as_dict(l)

            if l is None:
                status_code = NOT_FOUND

    elif request.method == 'DELETE':
        l = list_dao.delete(list_id)
        result = get_list_as_dict(l)

        if l is None:
            status_code = NOT_FOUND

    response = jsonify({'item': result})
    response.status_code = status_code

    return response

def get_list_as_dict(l):
    if l is None:
        return {}
    val = {'id': l.id, 'name': l.name, 'update_date': l.update_date, 'create_date': l.create_date}
    return val
