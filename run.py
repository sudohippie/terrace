__author__ = 'Raghav Sidhanti'

from terrace import flask_app


def db_config():
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

if __name__ == "__main__":
    print flask_app.url_map
    flask_app.run()
