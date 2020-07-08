class Config(object):
    DEBUG = True

class DevConf(Config):
    DEBUG = True

class ProdConf(Config):
    DEBUG = False
