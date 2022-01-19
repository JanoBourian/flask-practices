from flask import Flask
from flask_restful import (
    Resource,
    Api,
)

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, name):
        return {"student": name}


# http://127.0.0.1:5000/student/Rolf
api.add_resource(Student, "/student/<string:name>")


if __name__ == "__main__":
    host = '192.168.0.20'
    port = '8080'
    debug = True
    app.run(host=host, port=port, debug=debug)