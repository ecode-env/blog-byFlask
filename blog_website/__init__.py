from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from flask_ckeditor import CKEditor
#from flask_gravatar import Gravatar

db = SQLAlchemy()
DB_NAME = "blog.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hello this is eyob from flask."
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config['CKEDITOR_PKG_TYPE'] = 'basic'
    db.init_app(app)

    CKEditor(app)
    # generate avatar image
    # gravatar = Gravatar(app,
    #                     size=100,
    #                     rating='g',
    #                     default='retro',
    #                     force_default=False,
    #                     force_lower=False,
    #                     use_ssl=False,
    #                     base_url=None)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    #import models
    from .models import User

    # initialize login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)



    create_database(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("instance/" + DB_NAME):
        with app.app_context():
            db.create_all()

        print('Database create successfully')
