from flask import Blueprint, render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from .model import User
from flask_login import login_user, logout_user, login_required
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/")
def login():
    return render_template('login.html')


@auth.route("/login", methods=['POST'])
def login_post():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, request.form.get('password')):
            login_user(user, remember=True)
            return redirect(url_for('main.index'))
        else:
            flash("Incorrect password pls try again")
            return redirect(url_for('auth.login'))
    else:
        flash("Invalid username pls try again")
        return redirect(url_for('auth.login'))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return 'logout'


@auth.route('/signup')
def sign_up():
    return render_template('register.html')


@auth.route('/signup', methods=['POST'])
def sign_up_post():
    if User.query.filter_by(email=request.form.get('email')).first():
        flash('Your Email is Registered with us')
        return redirect(url_for('auth.login'))
    new_user = User(request.form.get('first_name'), request.form.get('last_name'), request.form.get('email'), generate_password_hash(request.form.get('password')), request.form.get('contact_no'))
    db.session.add(new_user)
    db.session.commit()
    flash("Successfully Registered Please Login to Continue")
    return redirect(url_for('auth.login'))
