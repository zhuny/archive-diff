from flask import Flask
from google.cloud import datastore


def create_app():
    app = Flask(__name__)

    from .view import init as view_init
    view_init(app)

    app.datastore = datastore.Client()

    return app


