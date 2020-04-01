from flask import Blueprint, render_template, session, g
from backend.models import Info, User

service_bp = Blueprint("service", __name__, url_prefix="/service")

from .appoint import *


def get_g():
    user = session.get("user_id")
    if user:
        g.user = User.query.filter_by(id=user).first()
    else:
        g.user = None


@service_bp.route("/homeservice")
def homeservice():
    serviceInfo = Info.query.filter_by(access=True).all()
    return render_template("service/homeservice.html", serviceInfo=serviceInfo)


# @service_bp.route('/homeservice/hour')
# def servicehour():
#     serviceInfo = Info.query.filter_by(access=True, ).all()
