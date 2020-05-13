import os

class Config:
    '''
    General configuration parent class
    '''
   
    COUNTRIES_BASE_URL='https://api.covid19api.com/countries'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
class TestConfig(Config):

    

 config_options = {
'development': DevConfig,
'production':  ProdConfig
'testing':  TestConfig
}   