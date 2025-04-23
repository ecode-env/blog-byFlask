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
    likes = db.relationship('Like', backref='user', passive_deletes=True)

    date = db.Column(db.DateTime(timezone=True), default=func.now())


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)

    # Foreign key linking to the User (author) who created this post.
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # One-to-many: A post can have many comments and likes.
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    likes = db.relationship('Like', backref='post', passive_deletes=True)



class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)

    # Foreign keys to link this comment to the user and post.
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())



class Like(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # A like associates a user and a post.
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
