from os import system
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class BitwiseOr(Resource):
    def get(self, arg1, arg2):
        return int(arg1) | int(arg2)


api.add_resource(BitwiseOr, '/or/<arg1>&<arg2>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6085)
