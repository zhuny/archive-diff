from flask import Flask
from google.cloud import datastore


def create_app():
    app = Flask(__name__)

    from .converter import init as convert_init
    convert_init(app)

    from .view import init as view_init
    view_init(app)

    from .before_request import init as request_init
    request_init(app)

    app.datastore = datastore.Client()

    return app


