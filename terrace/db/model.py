__author__ = 'Raghav Sidhanti'

from terrace import flask_app
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(flask_app)


class List(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=150), nullable=False)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    items = db.relationship('Item')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<List %r>' % self.name

    def to_dict(self):
        items_dict = []
        if self.items:
            for item in self.items:
                items_dict.append(item.to_dict())

        result = {'id': self.id,
                  'name': self.name,
                  'update_date': self.update_date,
                  'create_date': self.create_date,
                  'items': items_dict}

        return result


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=150), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)
    is_complete = db.Column(db.Boolean, nullable=True)
    complete_date = db.Column(db.DateTime, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Item %r>' % self.name

    def to_dict(self):
        result = {'id': self.id,
                  'name': self.name,
                  'list_id': self.list_id,
                  'is_complete': self.is_complete,
                  'complete_date': self.complete_date,
                  'due_date': self.due_date,
                  'update_date': self.update_date,
                  'create_date': self.create_date}

        return result



if __name__ == '__main__':
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    # db.create_all()

    l = List('hello ')
    db.session.add(l)

    print List.query.all()
