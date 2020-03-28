from flask import Blueprint, g, redirect, render_template, session, url_for
from backend.models import User

manage_bp = Blueprint("manage", __name__, url_prefix="/manage")
from .service import *


@manage_bp.before_request
def require_manager():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect(url_for("auth.login"))
    else:
        # print(user_id)
        user = User.query.filter_by(id=user_id).first()
        g.user = user
        if user.level >= User.LEVEL.get("MANAGE_LOW"):
            pass
        else:
            return redirect(url_for("auth.login"))


@manage_bp.route("/")
def index():
    user = User.query.filter_by(level=1).all()
    user.extend(User.query.filter_by(level=2).all())
    return render_template("manage/index.html", userInfo=user)
