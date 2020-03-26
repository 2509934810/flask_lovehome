from flask import Blueprint, g, render_template, session, redirect, url_for, request, g
from werkzeug.security import check_password_hash
from hashlib import md5
import os
from backend import db
from backend.models import User
from backend import redis_store, celery
from celeryWorker import sendMail
from backend.models import User
import random

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

from .index import indexs
from .UserCrud import addUser

# 随机生成url 调用celery给管理员发送邮件
def create_randomurl():
    BaseUrl = md5()
    BaseUrl.update("{}".format(random.randrange(1000, 100000)).encode("utf-8"))
    sendMail(
        text="Dear admin your login url is http://127.0.0.1:5000/admin/{}/login".format(
            BaseUrl.hexdigest()
        ),
        sender="2509934810@qq.com",
        receiver="mr zhang",
        subject="authentical_email",
        address="2509934810@qq.com",
    )
    return BaseUrl.hexdigest()


@admin_bp.route("/")
def index():
    BaseUrl = create_randomurl()
    redis_store.set("loginRoute", BaseUrl, ex=300)
    return redirect(url_for("auth.login"))


@admin_bp.before_request
def checkIfRoot():
    AllowUrl = []
    loginRoute = redis_store.get("loginRoute")
    if loginRoute:
        AllowUrl.append(
            "{}/admin/{}/login".format(
                "http://127.0.0.1:5000", loginRoute.decode("utf-8")
            )
        )
    AllowUrl.append("{}/admin/".format("http://127.0.0.1:5000"))
    if request.url not in AllowUrl:
        print(request.url, AllowUrl)
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
        print("l")
        if route == acceptRoute:
            return render_template("admin/login.html")
        else:
            return redirect(url_for("auth.login"))
