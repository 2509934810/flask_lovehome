from flask import request, redirect, render_template, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask import g

from backend.auth import auth_bp
# from backend.models import User

@auth_bp.route('/login', methods=("GET", "POST"))
def login():
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username is None:
            error = 'Username is required'
        elif password is None:
            error = 'Password is required'
        if error:
            db_userinfo = User.query.filter_by(username = username).first()
            if db_username:
                if check_password_hash(db_userinfo['password'], password):
                    return redirect(url_for('index'))
        return redirect('you have login')
    return render_template('auth/login.html')
