# config file(https://qiita.com/nanakenashi/items/e272ff1aafb3889230bc?msclkid=462df270c39f11ec92157f4731435d3a)

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI="sqlite:///data\\user_database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # autoincrement
    SQLALCHEMY_ECHO=True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING= False
    SQLALCHEMY_DATABASE_URI="sqlite:///..\\..\\data\\user_database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # autoincrement
    SQLALCHEMY_ECHO=True

class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI="sqlite:///data\\user_database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # autoincrement
    SQLALCHEMY_ECHO=True
