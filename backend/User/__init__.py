from flask import Blueprint, g, session, redirect, url_for, render_template
from backend.models import User

user_bp = Blueprint("user", __name__, url_prefix="/user")

from .UserSecurity import security
from .UserActived import actived
from .UserService import service


@user_bp.before_request
def check_user_login():
    userId = session.get("user_id")
    if userId is None:
        g.user = None
        print(url_for("auth.login"))
        return redirect(url_for("auth.login"))
    else:
        g.user = User.query.filter_by(id=userId).first()


@user_bp.route("/")
def index():
    return render_template("User/index.html")
