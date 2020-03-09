from flask import Blueprint, g, render_template, session, redirect, url_for, request, g
from werkzeug.security import check_password_hash
from hashlib import sha1
import os
from backend import db
from backend.models import User
from backend import redis_store, celery
from celeryWorker import sendMail
from backend.models import User


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

from .index import indexs
from .UserCrud import addUser

# @celery.task()
def create_randomurl():
    BaseUrl = sha1().hexdigest()
    sendMail.delay(
        text="Dear admin your login url is http://127.0.0.1:5000/admin/{}/login".format(
            BaseUrl
        ),
        sender="qq2509934810@163.com",
        receiver="mr zhang",
        subject="authentical_email",
        address="2509934810@qq.com",
    )
    # client = SendMail(
    #     text="Dear admin your login url is http://127.0.0.1:5000/admin/{}/login".format(
    #         BaseUrl
    #     ),
    #     sender="qq2509934810@163.com",
    #     receiver="mr zhang",
    #     subject="authentical_email",
    #     address="2509934810@qq.com",
    # )
    # client.send()
    return BaseUrl


@admin_bp.route("/")
def index():
    BaseUrl = create_randomurl()
    redis_store["loginRoute"] = BaseUrl
    return redirect(url_for("auth.login"))


@admin_bp.before_request
def checkIfRoot():
    if request.url != "/admin":
        userId = session.get("user_id")
        if userId:
            user = User.query.filter_by(id=userId).first()
            if user.level == User.LEVEL.get("ADMIN"):
                g.user = user
            else:
                return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.login"))


@admin_bp.route("/<route>/login", methods=["POST", "GET"])
def login(route):
    if request.method == "POST":
        account = request.form["account"]
        password = request.form["password"]
        admin = User.query.filter_by(account=account).first()
        if admin:
            if check_password_hash(admin.password, password):
                if User.checkRoot(User.LEVEL.get("ADMIN"), admin.level):
                    session["user_id"] = admin.id
                    return redirect(url_for("admin.indexs"))
                else:
                    return redirect(url_for("auth.login"))
            else:
                return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.login"))
    else:
        acceptRoute = redis_store.get("loginRoute").decode("utf-8")
        if route == acceptRoute:
            return render_template("admin/login.html")
        else:
            return redirect(url_for("auth.login"))
