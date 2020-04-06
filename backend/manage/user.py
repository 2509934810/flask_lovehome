from . import manage_bp
from flask import render_template, redirect, g
from backend.models import User, workrel


@manage_bp.route("/user")
def getuser():
    userList = set([user.workerId for user in g.user.manId.all()])
    userInfo = User.query.filter(User.account.in_(userList))
    return render_template("manage/user.html", userInfo=userInfo)
