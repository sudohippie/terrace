__author__ = 'Raghav Sidhanti'

from terrace.db.model import db, List


def _commit():
    db.session.commit()


def get_all_lists():
    return List.query.all()


def save_list(name):
    l = List(name)
    db.session.add(l)
    _commit()
    return l


def get_list_by_id(list_id):
    return List.query.get(list_id)


def update_list(list_id, name):
    l = get_list_by_id(list_id)
    l.name = name
    db.session.add(l)
    _commit()
    return l


def delete_list(list_id):
    l = get_list_by_id(list_id)

    if l is None:
        return None

    db.session.delete(l)
    _commit()
    return l