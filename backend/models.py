from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from backend import db


class User(db.Model):
    LEVEL = {
        "USER_LOW": 1,
        "USER_MID": 2,
        "WORKER": 4,
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
    telephone = db.Column(db.String(15), nullable=True)
    level = db.Column(db.Integer, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # head_photo = db.relationship('Photo', backref='user', lazy='dynamic')
    extra_info = db.relationship("WorkerServiceInfo", backref="user", lazy="dynamic")
    salary_info = db.relationship("Salary", backref="user", lazy="dynamic")
    actived = db.Column(db.Boolean, nullable=False, default=False)
    loginInfo = db.relationship("loginTb", backref="user", lazy="dynamic")
    sex = db.Column(db.Boolean, nullable=True)
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

    def updateInfo(self, username, email, telephone, sex, age, actived):
        self.username = username
        self.email = email
        self.telephone = telephone
        self.sex = sex
        self.age = age
        self.actived = actived

    @staticmethod
    def checkRoot(DbLevel, UserLevel):
        return DbLevel == UserLevel


class WorkerServiceInfo(db.Model):
    __tablename__ = "Info"
    TIMETYPE = {
        # 家政保姆
        "H_WORKER": 1,  # 小时工
        "H_WORKER_H": 4,  # 高级小时工
        "M_WORKER": 2,  # 月
        "M_WORKER_H": 8,  # 月 高级
    }
    SERVICETYPE = {
        "CLEANER": 1,  # 清洁工
        "BAOJIE": 2,  # 保洁
    }
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    head_photo = db.Column(db.String(30), nullable=False)
    timeType = db.Column(db.Integer, nullable=False, default=1)
    serviceType = db.Column(db.Integer, nullable=False, default=1)
    live_addr = db.Column(db.Text, nullable=False)
    avg_salary = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    access = db.Column(db.Boolean, nullable=False, default=False)

    def createInfo(self, head_photo, serviceType, live_addr, user_id, salary, timeType):
        self.user_id = user_id
        self.head_photo = head_photo
        self.live_addr = live_addr
        self.timeType = timeType
        self.serviceType = self.SERVICETYPE.get(serviceType)
        self.avg_salary = self._salary(salary, timeType)

    def activeAcc(self, set=False):
        if set:
            self.access = True
        else:
            self.access = False

    def changeTimeType(self, timeType):
        self.timeType = self.TIMETYPE.get(timeType)

    def _salary(salary, timeType, radio=1.5):
        if self.TIMETYPE.get(timeType) > 2:
            return salary * radio


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


# create db
class Service(db.Model):
    SERVICE = {
        "LOADING": 1,
    }
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provider = db.Column(db.String(20), db.ForeignKey("user.account"))
    shoper = db.Column(db.String(20), db.ForeignKey("user.account"))
    serviceType = db.Column(db.Integer, nullable=False, default=1)
    createTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
