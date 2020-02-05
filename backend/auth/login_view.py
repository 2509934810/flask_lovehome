from flask import request, redirect, render_template, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask import g

from backend.auth import auth_bp
from backend.models import User
from backend import db


@auth_bp.route("/login", methods=("GET", "POST"))
def login():
    error = None
    if request.method == "POST":
        account = request.form["account"]
        password = request.form["password"]
        if account is None:
            error = "account is required"
        elif password is None:
            error = "Password is required"
        else:
            db_userinfo = User.query.filter_by(account=account).first()
            if db_userinfo is None:
                error = "user not exist"
            elif check_password_hash(db_userinfo.password, password):
                session["user_id"] = db_userinfo.id
                return redirect(url_for("index"))
            else:
                error = "password error"
        flash(error)
        return redirect(url_for("auth.login"))
    return render_template("auth/login.html")
