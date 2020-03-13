from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from backend import db


class User(db.Model):
    LEVEL = {
        "USER_LOW": 1,
        "USER_MID": 2,
        "USER_HIG": 4,
        "MANAGE_LOW": 8,
        "MANAGE_MID": 16,
        "MANAGE_HIG": 32,
        "ADMIN": 64,
    }

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(20), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(30), nullable=True)
    telephone = db.Column(db.Integer, nullable=True)
    level = db.Column(db.Integer, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # head_photo = db.relationship('Photo', backref='user', lazy='dynamic')
    extra_info = db.relationship("Info", backref="user", lazy="dynamic")
    salary_info = db.relationship("Salary", backref="user", lazy="dynamic")
    actived = db.Column(db.Boolean, nullable=False, default=False)
    loginInfo = db.relationship("loginTb", backref="user", lazy="dynamic")
    sex = db.Column(db.Boolean, nullable=False)
    age = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return "<Post %r>" % self.account

    def createUser(self, account, password, role, username):
        self.account = account
        self.password = password
        self.level = self.LEVEL.get(role)
        self.username = username

    def addPermission(self, role):
        self.level = self.LEVEL.get(role)

    def revertPermission(self):
        self.level = self.LEVEL.get("USER_LOW")

    @staticmethod
    def checkRoot(DbLevel, UserLevel):
        return DbLevel == UserLevel


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    head_photo = db.Column(db.Binary, nullable=False)
    live_addr = db.Column(db.Text, nullable=True)
    avg_salary = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    send_date = db.Column(db.DateTime, nullable=False)
    salary_num = db.Column(db.Float, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


# add worker table


class loginTb(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    loginTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    loginSite = db.Column(db.Text, nullable=False, default="shanxi")

    def createData(self, userId, loginSite):
        self.user_id = userId
        self.loginSite = loginSite
