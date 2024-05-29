import os

class Config: # Define Config class to store variables for Flask app
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
