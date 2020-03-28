from . import manage_bp
from flask import render_template, redirect, g, url_for, request, jsonify, session
from backend.models import User, Info
from backend import db
import os, random


@manage_bp.route("/service")
def service():
    serviceInfo = Info.query.filter_by(access=False).all()
    return render_template("manage/service.html", serviceInfo=serviceInfo)


@manage_bp.route("/service/spread")
def spread():
    if g.user.level < 32:
        return redirect(url_for("auth.login"))
    rsp = {}
    userList = User.query.filter_by(level=1).all()
    rsp["user"] = userList
    userList = User.query.filter_by(level=4).all()
    rsp["worker"] = userList
    userList = User.query.filter_by(level=8).all()
    rsp["manage_low"] = userList
    userList = User.query.filter_by(level=16).all()
    rsp["manage"] = userList
    return render_template("manage/spreadService.html", userInfo=rsp)


@manage_bp.route("/service/worker")
def worker():
    return render_template("manage/workerman.html")


@manage_bp.route("/service/add", methods=["POST", "GET"])
def addservice():
    if request.method == "GET":
        user = User.query.filter_by(level=4).all()
        return render_template("manage/sendService.html", workers=user)
    else:
        user_account = request.form["worker"]
        timeType = request.form["timeType"]
        serviceType = request.form["serviceType"]
        img = request.files.get("upload")
        fileend = img.filename.split(".")[1]
        if fileend not in ["jpg", "png", "jpeg"]:
            return redirect(url_for("manage.index"))
        else:
            # add service todo
            service = Info()
            basepath = os.path.abspath(os.path.curdir)
            photopath = os.path.join(
                basepath,
                "backend/static/img/{}-{}.jpg".format(
                    worker, random.randrange(1, 100000)
                ),
            )
            headPhotoPath = photopath.split("static/")[1]
            # print(headPhotoPath, serviceType, timeType)
            print(g.user.id)
            service.createInfo(
                head_photo=headPhotoPath,
                serviceType=serviceType,
                live_addr="aa",
                user_id=g.user.id,
                user_account=user_account,
                salary=200,
                timeType=timeType,
            )
            db.session.add(service)
            db.session.commit()
            img.save(photopath)
            return redirect(url_for("manage.service"))
        return jsonify(request.form)
