from os import getenv
from datetime import timedelta


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv('JWT_SECRET')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=2)
    MAIL_SERVER = getenv('MAIL_SERVER')
    MAIL_PORT = getenv('MAIL_PORT')
    MAIL_USE_TLS = bool(getenv('MAIL_USE_TLS'))
    MAIL_USERNAME = getenv('MAIL_USERNAME')
    MAIL_PASSWORD = getenv('MAIL_PASSWORD')
    SECRET_KEY_SOCKET = getenv('SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL').replace(
    #     'postgres', 'postgresql', 1
    # )
    # PROPAGATE_EXCEPTIONS = True


config_env = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
