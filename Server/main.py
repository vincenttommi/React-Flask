from flask import Flask
from flask_restx import Api,Resource
from config import DevConfig 


app=Flask(__name__)
#initailising our app with the name


app.config.from_object(DevConfig)
api=Api(app, doc='/docs')
#creating an instance of our api

@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello World"}
    
    
    
if __name__ == '__main__':
    app.run()    