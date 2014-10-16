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

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=150), nullable=False)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Item %r>' % self.name


if __name__ == '__main__':
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    # db.create_all()

    l = List('hello ')
    db.session.add(l)

    print List.query.all()
