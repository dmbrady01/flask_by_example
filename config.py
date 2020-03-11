import os
basedir: str = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG: bool = False
    DEVELOPMENT: bool = False
    TESTING: bool = False
    CSRF_ENABLED: bool = True
    SECRET_KEY: str = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI: str = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
