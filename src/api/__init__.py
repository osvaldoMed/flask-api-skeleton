import os
from flask import Flask, jsonify
#from .config import Config as conf



def create_app(config):
    app = Flask(__name__)

    @app.route("/api/test_route", methods=["GET"])
    def sample_route():
        message = f"This is a sample route for {config.ENVIRONMENT}"
        app_secret = os.getenv('APP_SECRET')
        response_dict = {"message": message,
                         "APP_SECRET": app_secret,
                         "APP_NAME": config.APP_NAME,
                         "ENVIRONMENT_OS": os.getenv('ENVIRONMENT'),
                         "ENVIRONMENT_CONFIG": config.ENVIRONMENT}
        return jsonify(response_dict)

    return app