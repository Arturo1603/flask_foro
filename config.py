from os import getenv


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG=True


class ProductionConfig(BaseConfig):
    DEBUG=False


config_env = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
