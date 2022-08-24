from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

"""
   A Class to return greek letter
   :return: json response
 """


class Greek(Resource):
    def get(self, letter):
        return jsonify({"choosen-letter": letter})


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.
    :return: Flask app
    """

    if settings_override:
        app.config.update(settings_override)
    return app


# Since its just a small Demo app we are not using Blueprint.
# But On production with larger application i would prefer to use Blueprints
api.add_resource(Greek, "/letter/<string:letter>", endpoint="api.letter")
