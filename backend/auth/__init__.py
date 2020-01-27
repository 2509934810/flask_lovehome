from flask import Blueprint, g, request, render_template, redirect
from flask import request, redirect, render_template, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask import g

# from backend.models import User
# from .login import login as login_func


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import login_view
from . import logout_view
from . import register_view

def required_login():
    pass