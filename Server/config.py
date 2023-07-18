from decouple import config
# helps to organize setting so that parameteres can be changed without  having to   
#redeploy my app

class Config:
    SECRET_KEY=config('SECRET_KEY')