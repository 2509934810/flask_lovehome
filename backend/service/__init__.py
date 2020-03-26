from flask import Blueprint, render_template

service_bp = Blueprint("service", __name__, url_prefix="/service")


@service_bp.route("/homeservice")
def homeservice():
    return render_template("service/homeservice.html")
