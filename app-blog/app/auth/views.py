from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from datetime import datetime
from .forms import LoginForm, RegistrationForm
from ..models import User
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next_route = request.args.get('next')
            if next_route is None or not next_route.startswith('/'):
                next_route = url_for('main.index')
            return redirect(next_route)
        flash('Invalid username or password')
    return render_template('auth/login.html', current_time = datetime.now(), form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now loging')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', current_time = datetime.now(), form = form)