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
    return render_template(
        "detail.html",
        page=PageController.get_by_id(page_id),
        last_rev=PageController.get_last_rev(page_id),
        rev_list=PageController.get_rev_list(page_id)
    )


@bp.route('/<int:page_id>/<int:rev1_id>/<int:rev2_id>')
def diff_rev(page_id, rev1_id, rev2_id):
    pass


def init(app: Flask):
    app.register_blueprint(bp)


