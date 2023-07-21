from decouple import config
# helps to organize setting so that parameteres can be changed without  having to   
#redeploy my app
import os 

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
#this method will get the realname of dirpath

class Config:   
    SECRET_KEY=config('SECRET_KEY')
    #setting sqlachemy track modifications
SQLALCHEMY_TRACK_MODOFICATIONS=config('SQLALECHMY_TRACK_MODIFICATIONS',cast=bool)




class DevConfig(Config):
    SQLACHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,'dev.db')
    DEBUG=True
    SQLACHEMY_ECHO=True
    
    
    

class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass    