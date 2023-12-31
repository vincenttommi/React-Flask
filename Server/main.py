from flask import Flask
from flask_restx import Api,Resource
from config import DevConfig 
from  models import Recipe
from exts import db


app = Flask(__name__)
#initailising our app with the name
db.init_app(app)
#initialising our application with sqlachemy


app.config.from_object(DevConfig)
api=Api(app,doc='/docs')
#creating first route our api
@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello World"}
    
    
    
    
    
    
    
    
@app.shell_context_processor    
def make_shell_context(): 
    return {
        "db":db,
        "Recipe":Recipe
    }   
#context processor helps us to  access db instance and models from exts 
    
if __name__ == '__main__':
    app.run()    