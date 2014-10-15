__author__ = 'Raghav Sidhanti'

from terrace.db import list_dao
from flask import Blueprint
from flask import request, jsonify, url_for
from httplib import BAD_REQUEST, NOT_FOUND

list_api = Blueprint('list_api', __name__)


@list_api.route('/lists', methods=['GET', 'POST'])
def all_lists():
    if request.method == 'GET':
        all_lists = list_dao.get_all_lists()
        results = []
        for l in all_lists:
            results.append(get_list_as_dict(l))

        return jsonify({'lists': results})

    elif request.method == 'POST':
        new_lists = request.json.get('lists')
        results = []
        for new_list in new_lists:
            l = list_dao.save_list(name=new_list.get('name'))
            results.append(get_list_as_dict(l))

        return jsonify({'lists': results})


@list_api.route('/list/<int:list_id>', methods=['GET', 'PUT', 'DELETE'])
def list_by_id(list_id):
    if request.method == 'GET':
        one_list = list_dao.get_list_by_id(list_id)
        res = jsonify(get_list_as_dict(one_list))

        if one_list is None:
            res.status_code = NOT_FOUND

        return res

    elif request.method == 'PUT':
        name = request.json.get('name')
        if name is None:
            resp = jsonify({'error': 'Name is required'})
            resp.status_code = BAD_REQUEST
            return resp
        else:
            l = list_dao.update_list(list_id=list_id, name=name)
            res = jsonify(get_list_as_dict(l))
            if l is None:
                res.status_code = NOT_FOUND
            return res

    elif request.method == 'DELETE':
        l = list_dao.delete_list(list_id)
        res = jsonify(get_list_as_dict(l))
        if l is None:
            res.status_code = NOT_FOUND
        return res


def get_list_as_dict(l):
    if l is None:
        return {}
    val = {'id': l.id, 'name': l.name, 'update_date': l.update_date, 'create_date': l.create_date}
    return val
