from flask import render_template
from backend.models import User
from . import admin_bp


@admin_bp.route("/indexs")
def indexs():
    users = User.query.filter_by(level=User.LEVEL.get("USER_LOW")).all()
    return render_template("admin/index.html", users=users)
