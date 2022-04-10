
import os

class BaseConfig:
    DEBUG = False
    TESTING = False

class DevelopmentConfig:
    DEBUG = True
    TESTING= False

class TestingConfig:
    DEBUG = False
    TESTING = True
