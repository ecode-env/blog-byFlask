from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .decorators import admin_required
from .models import Post, Comment, Like
from . import db

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
@login_required
def home():
    post = Post.query.all()
    return render_template(template_name_or_list='home.html', user=current_user, posts=post)


@views.route('/create-post', methods=['GET','POST'])
@login_required
@admin_required
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
                author_id=current_user.id
            )
            db.session.add(post)
            db.session.commit()
            flash(message='Post Created', category='success')
            return redirect(url_for('views.home'))

    return render_template('create_post.html', user=current_user)

@views.route("/post/<int:post_id>")
@login_required
def post(post_id):
    get_post = Post.query.filter_by(id=post_id).first_or_404()
    return render_template('post.html', user=current_user, post=get_post)

# Delete route

@views.route('/delete-post/<id>')
@login_required
@admin_required
def delete_post(id):
    try:
        post = Post.query.filter_by(id=id).first()
        if not post:
            flash('Post not found!', category='error')
            return redirect(url_for('views.home'))


        Comment.query.filter_by(post_id=id).delete()

        db.session.delete(post)
        db.session.commit()

        flash('Post and associated comments deleted!', category='success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting post: {str(e)}', category='error')

    return redirect(url_for('views.home'))

# Create comment

@views.route('/post/comment/<int:post_id>', methods=['GET', 'POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('comment')
    if not text:
        flash(message='Comment cannot be empty!', category='error')
    else:
        post = Post.query.filter_by(id=post_id).first()
        if not post:
            flash(message='Post doesnt exist!', category='error')
        else:
            comment = Comment(
                text=text,
                author_id=current_user.id,
                post_id=post_id
                )
            db.session.add(comment)
            db.session.commit()
            flash(message='Your comment posted', category='success')


    return redirect(request.referrer or url_for('views.home'))

# edit comment

@views.route('/comment/<int:comment_id>/edit', methods=['POST'])
@login_required
def edit_comment(comment_id):
    # Check if comment exists
    comment = Comment.query.get(comment_id)
    if not comment:
        flash('Comment not found', category='error')
        return redirect(request.referrer)

    # Authorization check
    if comment.author_id != current_user.id:
        flash('You cannot edit another user\'s comment', category='error')
        return redirect(request.referrer)

    new_text = request.form.get('comment-text', '').strip()

    # Check if new text is empty
    if not new_text:
        flash('Comment cannot be empty', category='error')
        return redirect(request.referrer)

    # Check if the new comment is the same as the old one
    if new_text == comment.text:
        flash('No changes made to the comment', category='info')
        return redirect(request.referrer)

    # Check for length constraints
    if len(new_text) < 3:
        flash('Comment must be at least 3 characters long', category='error')
        return redirect(request.referrer)
    if len(new_text) > 500:
        flash('Comment is too long (maximum 500 characters)', category='error')
        return redirect(request.referrer)

    # Update the comment
    comment.text = new_text
    db.session.commit()

    flash('Comment updated successfully', category='success')
    return redirect(request.referrer)

# delete comment

@views.route('/comment/<int:comment_id>/delete')
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    if comment.author_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this comment.', 'error')
        return redirect(request.referrer or url_for('views.home'))

    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully.', 'success')
    return redirect(request.referrer or url_for('views.home'))


# Like post

@views.route('/like/<int:post_id>')
@login_required
def like_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        flash('Post doesn’t exist!', 'error')
        return redirect(url_for('views.home'))

    like = Like.query.filter_by(author_id=current_user.id, post_id=post_id).first()
    if like:
        db.session.delete(like)
        flash('Post unliked.', 'success')
    else:
        like = Like(author_id=current_user.id, post_id=post_id)
        db.session.add(like)
        flash('Post liked!', 'success')

    db.session.commit()
    # Redirect to referrer if valid, otherwise home
    referrer = request.referrer or url_for('views.home')
    if '/post/' in referrer:
        return redirect(url_for('views.post', post_id=post_id))
    return redirect(referrer)














