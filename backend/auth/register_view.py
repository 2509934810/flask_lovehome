from flask import request, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os

from . import auth_bp
from backend.models import User
from backend import db

@auth_bp.route('/register', methods=("GET", "POST"))
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username is None:
            error = 'username is required'
        elif password is None:
            error = 'password is required'
        else:
            if User.query.filter_by(username=username).first():
                error = 'username have existed'
            else:
                user = User(username=username, password = generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
                flash('you have registed')
                return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')