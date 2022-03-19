from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    response = make_response(request.headers.get("User-Agent"))
    response.set_cookie('answer', '42')
    return response

@app.route("/user/<name>")
def user(name):
    return "<h1> Hello {}! </h1>".format(name)

if __name__ =="__main__":
    args = {
    "debug":True,
    "port": '8000',
    "host": '192.168.0.22'
    }
    app.run(**args)