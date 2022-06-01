from datetime import datetime
from flask import render_template
from .forms import NameForm
from . import main 

@main.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', current_time=datetime.utcnow()), 200