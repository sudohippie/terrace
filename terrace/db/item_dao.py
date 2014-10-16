__author__ = 'Raghav Sidhanti'

from terrace.db.model import db, Item
from datetime import datetime


def get_all_items():
    return Item.query.all()


def save_item(**kwargs):
    name = kwargs.get('name')
    is_complete = kwargs.get('is_complete')
    complete_date = kwargs.get('compete_date')
    due_date = kwargs.get('due_date')

    i = Item(name, is_complete, complete_date, due_date)

    db.session.add(i)
    db.session.commit()

    return i


def get_item_by_id(item_id):
    if item_id is None:
        return None

    return Item.query.get(item_id)


def update_item(**kwargs):
    item_id = kwargs.get('item_id')

    i = get_item_by_id(item_id)

    if i is None:
        return None

    if 'name' in kwargs:
        i.name = kwargs.get('name')

    if 'is_complete' in kwargs:
        is_complete = kwargs.get('is_compete')
        if is_complete:
            if i.is_complete is None or not i.is_complete:
                i.is_complete = True
                i.complete_date = datetime.now()
        else:
            i.is_complete = False
            i.complete_date = None

    if 'due_date' in kwargs:
        i.due_date = kwargs.get('due_date')

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

