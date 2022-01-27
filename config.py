import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    # FLASK_DEBUG = environ.get('FLASK_DEBUG')
    FLASK_DEBUG = False


    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'mail.dikedim.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')or 'shout@dikedim.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False
    TESTING = False
    MAIL_ASCII_ATTACHMENTS = True
    MAP_BOX_KEY = os.environ.get('MAP_BOX_KEY')
    HCAPTCHA_ENABLED = True
    HCAPTCHA_SITE_KEY = os.environ.get('HCAPTCHA_SITE_KEY')
    HCAPTCHA_SECRET_KEY = os.environ.get('HCAPTCHA_SECRET_KEY')

    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')

    #APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    JOB_IMAGES = environ.get('JOB_IMAGES')
    #JOB_IMAGES = os.path.join(APP_ROOT, os.environ.get('JOB_IMAGES'))
    CLIENT_IMAGES = os.environ.get('CLIENT_IMAGES')
    BLOG_IMAGES = environ.get('BLOG_IMAGES')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')


class ProductionConfig(Config):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    pass


class DevelopmentConfig(Config):
    MAP_BOX_KEY = os.environ.get('MAP_BOX_KEY')
    MAP_BOX = os.getenv('MAP_BOX_KEY')
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    FLASK_DEBUG = True
    MAIL_SUPPRESS_SEND = False
    TESTING = False
    JOB_IMAGES = os.environ.get('JOB_IMAGES')


class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
    FLASK_DEBUG = True


