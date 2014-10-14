__author__ = 'Raghav Sidhanti'

from flask import Flask

flask_app = Flask(__name__)

# all modules must be added to package for the system to work
import terrace.api.list