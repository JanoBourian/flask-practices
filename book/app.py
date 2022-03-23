from flask import Flask, request, make_response, render_template

app = Flask(__name__)

user_list = [
    {'name': "Jonh", "filePhotoName": "jonh_book"},
    {'name': "Carl", "filePhotoName": "carl_book"},
    {'name': "Gretta", "filePhotoName": "gretta_book"},
    ]

@app.route("/")
def index():
    return render_template('index.html', user_list=user_list)

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
    "host": '192.168.0.22'
    }
    app.run(**args)