from datetime import datetime
from flask import render_template, session, flash, redirect, url_for, current_app
from .forms import NameForm
from ..email import send_email
from . import main 
from .. import db
from ..models import User, Role

@main.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
            flash('Looks like you have changed your name!')
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for("main.index"))
    return render_template('index.html', current_time=datetime.utcnow(), known=session.get('known', False), form = form, name=session.get('name', '')), 200