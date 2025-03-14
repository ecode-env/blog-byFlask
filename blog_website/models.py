from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)  # Admin field

    # Relationships: A user can have many posts, comments, and likes.
    posts = db.relationship('Post', backref='author', passive_deletes=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    author = db.relationship('User', backref='posts')
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    comments = db.relationship('Comment', backref='post', passive_deletes=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    commented_by = db.relationship('User', backref='comment',  passive_deletes=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
