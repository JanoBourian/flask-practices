from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Hello, world! </html>'

if __name__ == '__main__':
    host = '127.0.0.1'
    port = '5000'
    debug = True
    app.run(host = host, port = port, debug = debug)