__author__ = 'Raghav Sidhanti'

from terrace import flask_app


if __name__ == "__main__":
    print flask_app.url_map
    flask_app.run()
