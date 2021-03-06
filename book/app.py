from flask import Flask, request, make_response, render_template, redirect, url_for, session, flash
from flask_moment import Moment 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from datetime import datetime
from threading import Thread
from config import (MAIL_USERNAME, MAIL_PASSWORD, FLASKY_ADMIN)
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "u}7BYJy(P@0UCpdSJF/4|s:pcf'oD7'I*_sTZjW)C|M|F0^K9WUQ&S~Ai=F6;!Q"

app.config["MAIL_SERVER"] = 'smtp.googlemail.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = MAIL_USERNAME
app.config["MAIL_PASSWORD"] = MAIL_PASSWORD
app.config["FLASKY_ADMIN"] = FLASKY_ADMIN
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

mail = Mail(app)
db = SQLAlchemy(app)
moment = Moment(app)
migrate = Migrate(app, db)
user_list = [
    {'name': "Jonh", "filePhotoName": "jonh_book"},
    {'name': "Carl", "filePhotoName": "carl_book"},
    {'name': "Gretta", "filePhotoName": "gretta_book"},
    ]

### Forms 
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()] )
    submit = SubmitField('Submit')

### Model Definition
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    users = db.relationship('User', backref='role', lazy='dynamic')
    
    def __repr__(self):
        return f"<Role {self.name}>"
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique = True, nullable = False, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return f"<User {self.name}>"    

### Auxiliar functions
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender = app.config['FLASKY_MAIL_SENDER'], recipients = [to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

### Views
@app.before_first_request
def set_info():
    session['name'] = ''

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if FLASKY_ADMIN:
                print(user.username)
                send_email(FLASKY_ADMIN, 'New User', 'mail/new_user', user = user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for("index"))
    return render_template('index.html', form = form, user_list=user_list, current_time = datetime.utcnow(), name = session.get('name', ''), known=session.get('known', False))

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error_server(e):
    return render_template('500.html'), 500

if __name__ =="__main__":
    args = {
    "debug":True,
    "port": '8000',
    "host": '192.168.0.26'
    }
    app.run(**args)