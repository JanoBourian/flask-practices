from flask import Flask, make_response, abort, request, render_template
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'R4U=ENgRe,-.#m{-w,M,J*pfZ-4V|G;;[WaaHH22Dex_$/eLhF*X(4B/vrI!KW7'
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name? ', max_length=50, validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/", methods=['GET'])
def index():
    list_of_items = ["Hello", "this", "is", "my", "name",]
    name = request.args.get('name', '')
    return render_template('index.html', name=name, list_of_items=list_of_items, current_time=datetime.utcnow())

@app.route("/user/<string:name>", methods=['GET'])
def user(name):
    is_json = make_response({"message": f"{name}"})
    print(type(is_json))
    print(type(is_json.get_json()))
    print(request)
    print(request.form)
    print(request.args)
    print(request.cookies)
    print(request.headers)
    print(type(request.headers))
    print(request.headers.get('Host', ''))
    print(request.files)
    print(request.get_data())
    print(request.blueprint)
    print(request.endpoint)
    print(request.method)
    print(request.scheme)
    print(request.is_secure)
    print(request.host)
    print(request.path)
    print(request.query_string)
    print(request.full_path)
    print(request.url)
    print(request.base_url)
    print(request.remote_addr)
    print(request.environ)
    return is_json

@app.route("/abort", methods=['GET'])
def abort_rule():
    # abort(400, description="This is not necessary")    
    abort(500, "My custom message")

@app.route("/set-cookie", methods=['GET'])
def set_cookie():
    print(f"Params: {request.args}")
    name = request.args.get('name', '')
    value = request.args.get('value', '')
    response = make_response('<h1>Hello my friend</h1>')
    if name and value:
        response.set_cookie(name, value)    
    else:
        response.set_cookie('this_is_the_name', 'this_is_the_value')
    return response, 200

@app.route("/delete-cookie", methods=['GET'])
def delete_cook():
    response = make_response('<h1>Hello, I removed the cookie</h1>')
    response.delete_cookie('this_is_the_name')
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', error=e), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html', error=e), 500


if __name__ == "__main__":
    app.run()