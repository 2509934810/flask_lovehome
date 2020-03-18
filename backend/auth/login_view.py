from flask import request, redirect, render_template, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask import g
import requests
import os
import logging
from backend.auth import auth_bp
from backend.models import User
from backend.models import loginTb
from backend import db


@auth_bp.route("/login", methods=("GET", "POST"))
def login():
    error = None
    if request.method == "POST":
        account = request.form["account"]
        password = request.form["password"]
        if account is None:
            error = "account is required"
        elif password is None:
            error = "Password is required"
        else:
            db_userinfo = User.query.filter_by(account=account).first()
            if db_userinfo is None:
                error = "user not exist"
            elif check_password_hash(db_userinfo.password, password):
                session["user_id"] = db_userinfo.id
                sinLogin = loginTb()
                # 调用高德api获取登录位置信息
                siteInfo = createSiteInfo()
                sinLogin.createData(userId=db_userinfo.id, loginSite=siteInfo)
                db.session.add(sinLogin)
                db.session.commit()
                return redirect(url_for("index"))
            else:
                error = "password error"
        flash(error)
        return redirect(url_for("auth.login"))
    return render_template("auth/login.html")


def createSiteInfo():
    remoteIp = request.remote_addr
    print(remoteIp)
    key = os.environ.get("GAODE_KEY")
    logging.info(key)
    url = "https://restapi.amap.com/v3/ip?key={}&ip={}&output=json".format(
        key, "114.247.50.2"
    )
    logging.info(url)
    result = requests.get(url).json()
    siteInfo = "省: {} 市: {}".format(result["province"], result["city"])
    return siteInfo
