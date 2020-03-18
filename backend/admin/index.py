from flask import render_template, request, redirect, url_for
from backend.models import User
from . import admin_bp


@admin_bp.route("/indexs")
def indexs():
    num = int(request.args.get("num", 0))
    userType = request.args.get("userType", "USER_LOW")
    selectId = request.args.get("selectId", 0)
    if selectId:
        try:
            selectId = request.args.get("selectId")
            users = User.query.filter_by(id=selectId).all()
            return render_template(
                "admin/index.html",
                users=users,
                userNum=len(users),
                curPage=0,
                curType=userType,
            )
        except:
            return redirect(url_for("admin.indexs"))
    else:
        users = User.query.filter_by(level=User.LEVEL.get(userType)).all()
        return render_template(
            "admin/index.html",
            users=users[num : num + 16],
            userNum=len(users),
            curPage=num,
            curType=userType,
        )
