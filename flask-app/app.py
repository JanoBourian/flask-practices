from flask import Flask, jsonify
from config.config import DevConfig

# Configurations
app = Flask(__name__)
app.config.from_object(DevConfig)

# Endpoints
@app.route("/", methods = ["GET"])
def stores():
    return jsonify({'message': 'Hello world!'})

# Functions
if __name__ == '__main__':
    app.run()