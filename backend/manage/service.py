from . import manage_bp
from flask import render_template, redirect, g, url_for, request, jsonify
from backend.models import User, WorkerServiceInfo
import os, random


@manage_bp.route("/service")
def service():
    return render_template("manage/service.html")


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
        worker = request.form["worker"]
        timeType = request.form["timeType"]
        serviceType = request.form["serviceType"]
        img = request.files.get("upload")
        filefront, fileend = img.filename.split(".")[0], img.filename.split(".")[1]
        if fileend not in ["jpg", "png", "jpeg"]:
            return redirect(url_for("manage.index"))
        else:
            # add service todo
            service = WorkerServiceInfo()
            # service.createInfo()
            basepath = os.path.abspath(os.path.curdir)
            photopath = os.path.join(
                basepath,
                "backend/static/img/{}-{}.jpg".format(
                    worker, random.randrange(1, 100000)
                ),
            )
            # with open(photopath, 'wb') as f:
            #     f.write(img.encode('utf-8'))
            img.save(photopath)
            return redirect(url_for("manage.addservice"))
        return jsonify(request.form)
