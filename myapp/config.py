class Config(object): 
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config): #configuramos el modo desarrollo, hay dos formas, debug o implementación
    DEBUG = True
