import os


class Config:
    """
    General configuration class
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")

class ProdConfig(Config):
    """
    Class for Production configurations. Child of Config class.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    """
    Class for Test configurations. Child of Config class.
    """
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://victormainak:password@localhost/mkondoni_test"

class DevConfig(Config):
    """
    Class for Development configurations. Child of Config class.
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://victormainak:password@localhost/mkondoni'
    DEBUG = True
    
config_options = {"development": DevConfig, "production": ProdConfig,"test": TestConfig}