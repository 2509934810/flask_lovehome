from . import service_bp
from flask import g, render_template, redirect, url_for, session, request
from backend.models import User, Info, Service
from backend import db


@service_bp.route("/appointment/<id>")
def appointment(id):
    info = Info.query.filter_by(id=id).first()
    userInfo = User.query.filter_by(account=info.user_account).first()
    if info:
        return render_template(
            "service/appointservice.html", serviceInfo=info, userInfo=userInfo
        )
    else:
        return redirect(url_for("pageNotFound"))


@service_bp.route("/appoint/<id>/confirm", methods={"GET", "POST"})
def confirmService(id):
    SERVICETYPE = {"清洁工": 1, "保姆": 2}
    TIMETYPE = {"小时工": 1, "普通": 2, "高级小时工": 4, "高级普通": 8}
    TIMECELL = {
        "小时工": "hour",
        "高级小时工": "hour",
        "普通": "month",
        "高级普通": "month",
    }
    if request.method == "POST":
        if session.get("user_id"):
            print(request.form)
            workerId = request.form["workerId"]
            serviceType = SERVICETYPE.get(request.form["serviceType"])
            # print(serviceType)
            timeType = request.form["timeType"]
            startTime = request.form["startTime"]
            # print(startTime)
            timeRange = request.form["timeRange"]
            myAddress = request.form["myAddress"]
            mytelephone = request.form["mytelephone"]
            cost = request.form["cost"]
            service = Service()
            service.create(
                customerId=g.user.account,
                providerId=workerId,
                serviceType=serviceType,
                TimeRange=timeRange,
                TimeCell=TIMECELL.get(timeType),
                ServiceAddr=myAddress,
                preStartTime=startTime,
                cost=cost,
                customerTel=mytelephone,
            )
            db.session.add(service)
            db.session.commit()
            return redirect(url_for("index"))
        else:
            return redirect(url_for("auth.login"))
    else:
        if session.get("user_id"):
            workInfo = Info.query.filter_by(id=id).first()
            userInfo = User.query.filter_by(id=session.get("user_id")).first()
            if workInfo:
                return render_template(
                    "service/confirmService.html", workInfo=workInfo, userInfo=userInfo
                )
            else:
                return redirect(url_for("pageNotFound"))
        else:
            return redirect(url_for("auth.login"))
