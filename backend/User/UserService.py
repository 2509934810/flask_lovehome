from flask import redirect, url_for, g, render_template
from . import user_bp

@user_bp.route('/service')
def service():
    return render_template('User/UserService.html')