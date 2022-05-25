from datetime import datetime
from flask import render_template, redirect, session, url_for, flash
from . import main
from .forms import NameForm
from .. import db
from ..models import User, Role

@main.route("/", methods=['GET', 'POST'])
def index():
    list_of_items = ["Hello", "this", "is", "my", "name",]
    form = NameForm()
    form.role.choices = [(rol.id, rol.name) for rol in Role.query.all()]
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            role = Role.query.filter_by(id=form.role.data).first()
            user = User(username=form.name.data, role=role)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            flash('Looks like you have changed your name!')
            # if app.config['FLASKY_ADMIN']:
            #     send_email(app.config['FLASKY_ADMIN'], 'New user added', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for("main.index"))
    return render_template('index.html', form=form, name=session.get('name', ''), list_of_items=list_of_items, current_time=datetime.utcnow(), known=session.get('known', False))
