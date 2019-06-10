from flask import render_template, redirect, Blueprint, request, url_for, flash, g
from qw.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from qw.db import mongo
from datetime import datetime
from qw.models import User

auth = Blueprint('auth', __name__, template_folder='../templates/auth', url_prefix='/auth')


@auth.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # password_hash = mongo.db.users['password'].find({'username': username})
        user = mongo.db.users.find_one({'username': username})
        password_hash = user['password']
        if user and check_password_hash(password_hash, password):
            login_user(User(user), 1)
            return redirect(request.args.get('next') or url_for('blog.index'))
        flash("Invalid username or password!")
    return render_template('login.html', form=form)


@auth.route('/register', methods=['get', 'post'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        password = register_form.password.data
        email = register_form.email.data
        new_user = {
            'username': username,
            'email': email,
            'password': generate_password_hash(password),
            'create_at': datetime.utcnow(),
            'is_active': True
        }
        mongo.db.users.insert_one(new_user)
        flash("Register successfully!")
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=register_form)


@auth.route('/logout', methods=['post', 'get'])
def logout():
    logout_user()
    return redirect(url_for('blog.index'))
