from flask import render_template
from . import auth
from datetime import datetime

@auth.route('/login')
def login():
    return render_template('auth/login.html', current_time = datetime.now())