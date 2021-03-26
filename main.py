from flask import Blueprint
from . import db
from flask_login import login_required, current_user
main = Blueprint("main", __name__)


@main.route("/index")
@login_required
def index():
    return 'index'


@main.route("/profile")
@login_required
def profile():
    return current_user.first_name
