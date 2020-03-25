from flask import jsonify
from backend.models import User
from . import api_bp


@api_bp.route("/findUser/<account>")
def findUser(account):
    data = {}
    user = User.query.filter_by(account=account).first()
    if user:
        data["code"] = 403
        data["info"] = "user exist"
        return jsonify(data)
    else:
        data["code"] = 200
        data["info"] = "用户可使用"
        return jsonify(data)
