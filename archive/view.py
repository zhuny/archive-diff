from flask import Blueprint, Flask

bp = Blueprint('archive', __name__)


@bp.route('/')
def index():
    pass


@bp.route('/<int:archive_id>')
def detail(archive_id):
    pass


@bp.route('/<int:archive_id>/<int:rev1_id>/<int:rev2_id>')
def diff_rev(archive_id, rev1_id, rev2_id):
    pass


def init(app: Flask):
    app.register_blueprint(bp)


