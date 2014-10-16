__author__ = 'Raghav Sidhanti'

from terrace.db.model import db, Item
from datetime import datetime


def get_all_items():
    return Item.query.all()


def save_item(**kwargs):
    name = kwargs.get('name')

    i = Item(name=name)

    db.session.add(i)
    db.session.commit()

    return i


def get_item_by_id(item_id):
    if item_id is None:
        return None

    return Item.query.get(item_id)


def update_item(item_id, name):

    i = get_item_by_id(item_id)

    if i is None:
        return None

    i.name = name

    db.session.add(i)
    db.session.commit()

    return i


def delete_item(item_id):
    i = get_item_by_id(item_id)

    if i is None:
        return None

    db.session.delete(i)
    db.session.commit()

    return i

