from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
