from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)

if __name__ =="__main__":
    args = {
    "debug":True,
    "port": '8000',
    "host": '192.168.0.22'
    }
    app.run(**args)