from flask import redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash
from . import admin_bp
from backend.models import User
from backend import db


@admin_bp.route("/user/add", methods=["GET", "POST"])
def addUser():
    if request.method == "POST":
        account = request.form["account"]
        username = request.form["username"]
        password = request.form["password"]
        level = request.form["level"]
        user = User()
        user.createUser(
            account=account,
            password=generate_password_hash(password),
            role=level,
            username=username,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("admin.indexs"))
    else:
        return render_template("admin/addUser.html")


@admin_bp.route("/delete/user", methods=["POST", "GET"])
def deleteUser():
    deleteIdStr = request.args.get("IdList")
    if deleteIdStr:
        deleteIdList = [int(id) for id in deleteIdStr.split(",")]
        # print(deleteId, type(deleteId))
        for deleteId in deleteIdList:
            user = User.query.filter_by(id=deleteId).first()
            if user is None:
                continue
            db.session.delete(user)
        db.session.commit()
        return redirect(url_for("admin.indexs"))
    else:
        return redirect(url_for("admin.indexs"))
