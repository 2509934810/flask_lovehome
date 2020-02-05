from flask import request, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os

from . import auth_bp
from backend.models import User
from backend import db
import random


@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        account = request.form["account"]
        password = request.form["password"]
        if username is None:
            error = "username is required"
        elif account is None:
            error = "account is required"
        elif password is None:
            error = "password id required"
        else:
            if User.query.filter_by(account=account).first():
                error = "username have existed"
            else:
                user = User(
                    account=account,
                    username=username,
                    password=generate_password_hash(password),
                    level=1,
                )
                db.session.add(user)
                db.session.commit()
                flash("you have registed")
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template("auth/register.html")
