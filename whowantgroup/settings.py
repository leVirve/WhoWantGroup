"""
settings.py

Configuration for Flask app

"""
from instance.config import CSRF_SECRET_KEY, SESSION_KEY


class Config(object):
    # Secret keys
    SECRET_KEY = CSRF_SECRET_KEY
    CSRF_SESSION_KEY = SESSION_KEY
    # Flask-Cache settings
    # CACHE_TYPE = 'gaememcached'


class Development(Config):
    DEBUG = True
    CSRF_ENABLED = True


class Testing(Config):
    TESTING = True
    DEBUG = True
    CSRF_ENABLED = True


class Production(Config):
    DEBUG = False
    CSRF_ENABLED = True
