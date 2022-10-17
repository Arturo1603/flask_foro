from os import getenv
from datetime import timedelta


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv('JWT_SECRET')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config_env = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
