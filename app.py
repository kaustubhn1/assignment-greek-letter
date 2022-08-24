from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
api = Api(app)


class Greek(Resource):

    def get(self, letter):

        return jsonify({'choosen-letter': letter})


api.add_resource(Greek, '/letter/<string:letter>')

# driver function
if __name__ == '__main__':

    app.run(debug=True)
