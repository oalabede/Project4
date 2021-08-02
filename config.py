"""App configuration."""
from os import environ, path

import redis
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration variables from .env file."""

    FLASK_APP = 'wsgi.py'
    FLASK_ENV = environ.get("FLASK_ENV")
    SECRET_KEY = environ.get("SECRET_KEY")

    REDIS_URI = environ.get("SESSION_REDIS")
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.from_url(REDIS_URI)

    LESS_BIN = environ.get("LESS_BIN")
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False