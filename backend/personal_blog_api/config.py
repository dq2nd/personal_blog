"""
config.py
- Settings for the flask application object
"""

class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///personalblog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # String is used for encryption and session management
    SECRET_KEY = 'puSCIAp7PvykT7w0d48U'

    BLOG_OWNER_EMAIL = 'doducanh2710@gmail.com'
    BLOG_OWNER_USERNAME = 'dq2nd'
    BLOG_OWNER_PASSWORD = '123456'
