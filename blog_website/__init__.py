from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

import app

db = SQLAlchemy()
DB_NAME = "blog.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hello this is eyob from flask."
    app.config["SQL_ALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    create_database(app)


    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app

def create_database(app):
    if not path.exists("blog_website/" + DB_NAME):
        db.create_all(app)
        print('Database create successfully')
