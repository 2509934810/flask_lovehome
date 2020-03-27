from flask import redirect, render_template, request, url_for, session

from . import user_bp
from backend.models import User
from backend import db


@user_bp.route("/actived", methods=["GET", "POST"])
def actived():
    sexDict = {1: True, 0: False}
    if request.method == "POST":
        # account = request.form['account']
        username = request.form["username"]
        sex = sexDict.get(request.form["sex"], True)
        age = request.form["age"]
        email = request.form["email"]
        telephone = request.form["telephone"]
        bornTime = request.form["bornTime"]
        idCard = request.form["idcard"]
        address = request.form["address"]
        if username and sex and email and telephone and bornTime and idCard and address:
            if checkInfo(username, idCard, bornTime, telephone, email):
                user = User.query.filter_by(id=session["user_id"]).first()
                actived = True
                user.updateInfo(username, email, telephone, sex, age, actived)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("user.index"))
        else:
            return render_template("User/UserActived.html")
        print(request.form, session["user_id"])
        return redirect(url_for("user.index"))
    else:
        return render_template("User/UserActived.html")


def checkId():
    pass


def checkInfo(username, idCard, bornTime, telephone, email):
    if username and idCard and bornTime and telephone and email:
        return True
    else:
        return False
