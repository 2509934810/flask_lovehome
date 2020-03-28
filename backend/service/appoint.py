from . import service_bp
from flask import g, render_template, redirect, url_for


@service_bp.route("/appointment")
def appointment():
    return render_template("service/appointservice.html")
