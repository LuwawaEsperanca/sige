from distutils.debug import DEBUG
import os
import config
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    CSRF_ENABLED =True
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "juddy"

    class ProductionConfig(Config):
        DEBUG = False
    class StagingConfig(Config):
        DEVELOPMENT = True
        DEBUG = True
    class DevelopmentConfig(Config):
        DEVELOPMENT = True
        BEBUG = True
    class TestingConfig(Config):
        TESTEING = True

    