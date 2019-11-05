from flask import Blueprint, Flask, render_template

from archive.controller import PageController

bp = Blueprint('archive', __name__)


@bp.route('/')
def index():
    return render_template(
        "index.html",
        page_list=PageController.get_list()
    )


@bp.route('/<int:page_id>')
def detail(page_id):
    pass


@bp.route('/<int:archive_id>/<int:rev1_id>/<int:rev2_id>')
def diff_rev(archive_id, rev1_id, rev2_id):
    pass


def init(app: Flask):
    app.register_blueprint(bp)


