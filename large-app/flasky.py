from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1> Hello world </h1>"

@app.route("/user/<string:name>")
def user(name:str):
    # print(request.args)
    return f"<h1> Hello {name}</h1>"

if __name__ == '__main__':
    args = {
    "debug":True,
    "port": '8000',
    "host": '192.168.0.26'
    }
    app.run(**args)