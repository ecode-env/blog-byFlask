from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hello this is eyob from flask."

    return app