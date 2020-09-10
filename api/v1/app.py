#!/usr/bin/python3
"""
Module that holds Flask REST_API
"""
from flask import Flask, Blueprint, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def close(error):
    """ Call method close() from storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ Response for error code 404 """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host, port, threaded=True)
