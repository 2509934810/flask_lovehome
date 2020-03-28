from flask import redirect, url_for, g, render_template
from . import user_bp
from backend.models import Info, User


@user_bp.route("/service")
def service():
    return render_template("User/UserService.html")


@user_bp.route("/service/myservice")
def myservice():
    userInfo = User.query.filter_by(id=g.user.id).first()
    print(userInfo.extra_info.first())
    user = Info.query.filter_by(user_id=g.user.id)
    print(user.all())
    return render_template("User/UserMyservice.html")
