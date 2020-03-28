from flask import Blueprint, render_template
from backend.models import Info

service_bp = Blueprint("service", __name__, url_prefix="/service")

from .appoint import *


@service_bp.route("/homeservice")
def homeservice():
    serviceInfo = Info.query.filter_by(access=True).all()
    return render_template("service/homeservice.html", serviceInfo=serviceInfo)
