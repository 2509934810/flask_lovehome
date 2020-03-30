from flask import redirect, url_for, g, render_template
from flask import request
from . import user_bp
from backend.models import Info, User, Service
from backend import db, redis_store
from datetime import datetime


@user_bp.route("/service")
def service():
    # print(g.user.account)
    services = Service.query.filter_by(providerId=g.user.account).all()
    return render_template("User/UserService.html", services=services)


@user_bp.route("/service/myservice")
def myservice():
    userInfo = User.query.filter_by(id=g.user.id).first()
    serviceInfo = userInfo.extra_info.all()
    # user = Info.query.filter_by(user_id=g.user.id)
    # print(user.all())
    return render_template(
        "User/UserMyservice.html", serviceInfo=serviceInfo, userInfo=userInfo
    )


@user_bp.route("/service/myservice/active/<id>")
def serviceActive(id):
    serviceInfo = Info.query.filter_by(id=id).first()
    serviceInfo.access = True
    db.session.add(serviceInfo)
    db.session.commit()
    return redirect(url_for("user.myservice"))


@user_bp.route("/service/start")
def start():
    user = User.query.filter_by(account=g.user.account).first()
    services = user.service.filter_by(orderType=2).all()
    print(services)
    return render_template("User/startService.html", services=services, user=user)


@user_bp.route("/service/startService/<id>")
def startService(id):
    service = Service.query.filter_by(id=id).first()
    service.orderType = 4
    service.startTime = datetime.utcnow()
    db.session.add(service)
    db.session.commit()
    return redirect(url_for("user.start"))


@user_bp.route("/service/doing")
def doing():
    user = User.query.filter_by(account=g.user.account).first()
    services = user.service.filter_by(orderType=4).all()
    # print(services)
    return render_template("User/doingService.html", services=services, user=user)


@user_bp.route("/service/closeservice/<id>", methods=["POST", "GET"])
def closeService(id):
    if request.method == "POST":
        service = Service.query.filter_by(id=id).first()
        if service:
            return redirect(url_for("user.nopay"))
        else:
            return redirect(url_for("pageNotFound"))
    else:
        service = Service.query.filter_by(id=id).first()
        if service:
            user = User.query.filter_by(account=g.user.account).first()
            # services = user.service.filter_by(orderType=4).all()
            # print(services)
            # serviceTime = datetime.now() - service.createTime
            serverTime = gettime(service.TimeCell, service.startTime)
            print(serverTime)
            avg_salary = service.salary / service.TimeRange
            salarySum = avg_salary * serverTime
            redis_store.set(service.id, salarySum, ex=300)
            redis_store.set(service.id + "time", serverTime, ex=300)
            return render_template(
                "User/confirmservice.html",
                service=service,
                user=user,
                serverTime=serverTime,
                salarySum=salarySum,
            )
        else:
            return redirect(url_for("pageNotFound"))


def gettime(Type, starttime):
    Cell = {
        "1": ((datetime.utcnow() - starttime).seconds) / 3600,
        "2": ((datetime.utcnow() - starttime).seconds) / 3600 / 24,
        "4": ((datetime.utcnow() - starttime).seconds) / 3600 / 24 / 30,
        "8": ((datetime.utcnow() - starttime).seconds) / 3600 / 24 / 365,
    }
    print(Cell.get(Type), Type, starttime, datetime.now())
    return Cell.get(Type)


@user_bp.route("/service/nopay")
def nopay():
    pass


# 模拟支付
@user_bp.route("/service/pay/<id>")
def pay(id):
    money = redis_store.get(id)
    time = redis_store.get(id + "time")
    if money:
        service = Service.query.filter_by(id=id).first()
        service.orderType = 16
        service.salary = money
        service.TimeRange = time
        service.endTime = datetime.utcnow()
        service.payTime = datetime.utcnow()
        db.session.add(service)
        db.session.commit()
        return redirect(url_for("user.doing"))
    else:
        return redirect(url_for("pageNotFound"))


@user_bp.route("/service/payed")
def payed():
    user = User.query.filter_by(id=g.user.id).first()
    services = user.service.filter_by(orderType=16).all()
    return render_template("User/payed.html", user=user, services=services)
