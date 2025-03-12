from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
@login_required
def home():
    return render_template(template_name_or_list='home.html', user=current_user)


@views.route('/create-post')
@login_required
def create_post():
    return render_template('create_post.html', user=current_user)