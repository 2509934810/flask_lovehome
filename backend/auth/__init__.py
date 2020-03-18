from flask import Blueprint, g, request, render_template, redirect
from flask import request, redirect, render_template, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask import g, session

from backend.models import User
# from .login import login as login_func


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import login_view
from . import logout_view
from . import register_view

def required_login():
    pass

@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()