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
    response = make_response('<h1>Hello my friend</h1>')
    response.set_cookie('this_is_the_name', 'this_is_the_value')
    return response, 200

@app.route("/delete-cookie", methods=['GET'])
def delete_cook():
    response = make_response('<h1>Hello, I removed the cookie</h1>')
    response.delete_cookie('this_is_the_name')
    return response

if __name__ == "__main__":
    app.run()