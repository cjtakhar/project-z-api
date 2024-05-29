from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # database instance 

def create_app(): # function configures instance of flask app 
    app = Flask(__name__) # creates instance of flask class
    app.config.from_object('config.Config') # load config settings 
    db.init_app(app) # initialize extensions
    from .routes import main as main_blueprint # register blueprints
    app.register_blueprint(main_blueprint)

    return app