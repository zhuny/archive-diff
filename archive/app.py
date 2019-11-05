from flask import Flask


def create_app():
    app = Flask(__name__)

    from .view import init as view_init
    view_init(app)

    return app


