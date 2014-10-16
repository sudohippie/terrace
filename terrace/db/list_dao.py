__author__ = 'Raghav Sidhanti'

from terrace.db.model import db, List


def get_all():
    return List.query.all()


def save(name):
    l = List(name)

    db.session.add(l)
    db.session.commit()

    return l


def get_by_id(list_id):
    return List.query.get(list_id)


def update(list_id, name):
    l = get_by_id(list_id)

    if l is None:
        return None

    l.name = name

    db.session.add(l)
    db.session.commit()

    return l


def delete(list_id):
    l = get_by_id(list_id)

    if l is None:
        return None

    db.session.delete(l)
    db.session.commit()

    return l