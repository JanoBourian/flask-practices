from flask import Flask, make_response, abort, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "<h1> Hello World! </h1>"

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
    return is_json

@app.route("/abort", methods=['GET'])
def abort_rule():
    # abort(400, description="This is not necessary")    
    abort(500, "My custom message")

if __name__ == "__main__":
    app.run()