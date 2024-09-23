import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', "a_very_secret_key")
    SERVER_HOST = os.environ.get('SERVER_HOST', 'localhost')
    SERVER_PORT = int(os.environ.get('SERVER_PORT', 5000))
    MONGO_URI = os.environ.get('MONGO_URI', "mongodb://localhost:27017/DigiMeet")