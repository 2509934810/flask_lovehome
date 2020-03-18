from flask import request, url_for, redirect, render_template, g
from . import user_bp
from backend.models import loginTb


@user_bp.route("/security")
def security():
    loginInfo = loginTb.query.filter_by(user_id=g.user.id).all()
    print(request.remote_addr)
    return render_template("User/UserSecurity.html", loginInfo=loginInfo)
