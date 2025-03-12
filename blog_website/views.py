from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
@login_required
def home():
    post = Post.query.all()
    return render_template(template_name_or_list='home.html', user=current_user, post=post)


@views.route('/create-post', methods=['GET','POST'])
@login_required
def create_post():
    if request.method == 'POST':
        content = request.form.get('content')
        title = request.form.get('title')

        if not content:
            flash(message='Content cannot be empty!', category='error')
        if not title:
            flash(message='Title cannot be empty!', category='error')
        else:
            post = Post(
                title=title,
                text=content,
                author=current_user.id
            )
            db.session.add(post)
            db.session.commit()
            flash(message='Post Created', category='success')
            return redirect(url_for('views.home'))

    return render_template('create_post.html', user=current_user)