from flask import Blueprint, g, redirect, render_template, session, url_for
from backend.models import User

manage_bp = Blueprint("manage", __name__, url_prefix="/manage")
from .service import *
from .user import *


@manage_bp.before_request
def require_manager():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect(url_for("auth.login"))
    else:
        # print(user_id)
        user = User.query.filter_by(id=user_id).first()
        g.user = user
        print(user.level > User.LEVEL.get("MANAGE_LOW"))
        if user.level >= User.LEVEL.get("MANAGE_LOW"):
            pass
        else:
            return redirect(url_for("auth.login"))


@manage_bp.route("/")
def index():
    user = []
    level = g.user.level
    if level == 64:
        pass
    if level == 32:
        pass
    elif level == 16:
        pass
    elif level == 8:
        usersL = getMan(g.user)
        for users in usersL:
            user.extend(getMan(users))
    else:
        return redirect(url_for("auth.login"))
    # user = User.query.filter_by(level=1).all()
    # user.extend(User.query.filter_by(level=2).all())
    return render_template("manage/index.html", userInfo=user)


def getMan(manAccount):
    manU = []
    userList = manAccount.manId.all()
    print(userList)
    for userl in userList:
        manU.append(User.query.filter_by(account=userl.workerId).first())
    manU = set(manU)
    return manU
