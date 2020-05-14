import os

class Config:
    '''
    General configuration parent class
    '''
    KENYAN_BASE_URL='https://coronavirus-19-api.herokuapp.com/countries/{}'
    COUNTRIES_BASE_URL='https://api.covid19api.com/countries'
    @staticmethod
    def init_app(app):
        pass

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

config_options = {
'development': DevConfig,
'production':  ProdConfig
}   