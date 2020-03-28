from flask import redirect, url_for, g, render_template
from . import user_bp
from backend.models import Info, User
from backend import db


@user_bp.route("/service")
def service():
    return render_template("User/UserService.html")


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
