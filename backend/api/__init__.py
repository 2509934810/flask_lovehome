from flask import Blueprint, g, session, jsonify, Response, request
from backend import auth_store
from backend.models import User
from werkzeug.security import check_password_hash, generate_password_hash
import hashlib

api_bp = Blueprint("api", __name__, url_prefix="/api")

from .find import *

forbeden = {"code": 403}


@api_bp.route("/register", methods=["POST"])
def register():
    data = {}
    formData = request.get_json(silent=True)
    username, account, password = (
        formData.get("username"),
        formData.get("account"),
        formData.get("password"),
    )
    user = User.query.filter(account=account).first()
    if user:
        data["code"] = 403
        data["info"] = "go out bitch"
        return jsonify(data)
    else:
        # todo add registry
        user = User()


@api_bp.route("/login", methods=["POST"])
def login():
    data = {}
    formData = request.get_json(silent=True)
    username, password = formData.get("username"), formData.get("password")
    user = User.query.filter_by(account=username).first()
    if user:
        if check_password_hash(user.password, password):
            data["code"] = 200
            data["token"] = createMd5(user)
            data["username"] = user.username
            data["account"] = user.account
            auth_store.set(user.account, data["token"], ex=600)
            data["debugInfo"] = "success"
            return jsonify(data)
        else:
            data["code"] = 403
            data["debugInfo"] = "password error"
            return jsonify(data)
    else:
        data["code"] = 403
        data["debugInfo"] = "user not exist"
        return jsonify(data)


def createMd5(user):
    md5 = hashlib.md5()
    md5.update("{}{}".format(user.account, "123456").encode("utf-8"))
    return md5.hexdigest()


@api_bp.route("/search")
def search():
    pass
