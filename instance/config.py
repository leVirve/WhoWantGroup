__author__ = 'Salas'

import os

CSRF_SECRET_KEY = 'once upon a time'
SESSION_KEY = ''


basedir = os.path.abspath(os.path.dirname(__file__))

MONGODB_SETTINGS = {
    'db': 'whowantgroup',
    'host': 'mongodb://localhost:27017'
}