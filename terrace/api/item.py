__author__ = 'Raghav Sidhanti'

from terrace.db import item_dao
from flask import Blueprint
from flask import request, jsonify
from httplib import BAD_REQUEST, NOT_FOUND, OK

item_api = Blueprint('item_api', __name__)


@item_api.route('/items', methods=['GET', 'POST'])
def all_items():
    results = None

    if request.method == 'GET':
        all = item_dao.get_all()
        for i in all:
            results.append(get_item_as_dict(i))

    elif request.method == 'POST':
        contents = request.json.get('lists')
        for content in contents:
            i = item_dao.save(name=content.get('name'))
            results.append(get_item_as_dict(i))

    return jsonify({'items': results})

@item_api.route('/item/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def item_by_id(item_id):
    result = {}
    status_code = OK

    if request.method == 'GET':
        one = item_dao.get_by_id(item_id)
        result = get_item_as_dict(one)

        if one is None:
            status_code = NOT_FOUND

    elif request.method == 'PUT':
        name = request.json.get('name')

        if name is None:
            status_code = BAD_REQUEST
        else:
            l = item_dao.update(item_id=item_id, name=name)
            result = get_item_as_dict(l)

            if l is None:
                status_code = NOT_FOUND

    elif request.method == 'DELETE':
        l = item_dao.delete(item_id)
        result = get_item_as_dict(l)

        if l is None:
            status_code = NOT_FOUND

    response = jsonify({'item': result})
    response.status_code = status_code

    return response

def get_item_as_dict(i):
    if i is None:
        return {}

    val = {'id': i.id, 'name': i.name, 'update_date': i.update_date, 'create_date': i.create_date}

    return val
