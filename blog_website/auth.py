import re
from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash,check_password_hash


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password')

        # Check if email and password are provided
        if not email or not password1:
            flash(message='Please provide both email and password.', category='error')
            return render_template('login.html',user=current_user)

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password1):
                flash(message='Logged in!', category='success')
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash(message='Password is incorrect!', category='error')
        else:
            flash(message='Email doesn\'t exist.', category='error')

    return render_template('login.html', user=current_user)



@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        # Validation checks
        if email_exists:
            flash(message='Email already exists. Please login.', category='error')
        elif username_exists:
            flash(message='Username is already in use.', category='error')
        elif password1 != password2:
            flash(message='Passwords do not match.', category='error')
        elif len(username) < 3:
            flash(message='Username must be at least 3 characters.', category='error')
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$', email):
            flash(message='Invalid email format.', category='error')
        elif len(password1) < 6:
            flash(message='Password must be at least 6 characters.', category='error')
        else:
            # noinspection PyArgumentList
            new_user = User(
                email=email,
                username=username,
                password=generate_password_hash(password1,method='pbkdf2:sha256'))

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash(message='Account created successfully!', category='success')
            return redirect(url_for('views.home'))

    return render_template('signup.html', user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))