from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from backend import db
from hashlib import md5
import random


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
    extra_info = db.relationship("Info", backref="user", lazy="dynamic")
    salary_info = db.relationship("Salary", backref="user", lazy="dynamic")
    actived = db.Column(db.Boolean, nullable=False, default=False)
    loginInfo = db.relationship("loginTb", backref="user", lazy="dynamic")
    sex = db.Column(db.Boolean, nullable=True)
    age = db.Column(db.Integer, nullable=False, default=0)
    service = db.relationship("Service", backref="user", lazy="dynamic")

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


# class WorkerInfo(db.Model):
#     pass


class Info(db.Model):
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
        "BAOMU": 2,  # bao
    }
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    head_photo = db.Column(db.String(80), nullable=False)
    timeType = db.Column(db.Integer, nullable=False, default=1)
    serviceType = db.Column(db.Integer, nullable=False, default=1)
    live_addr = db.Column(db.Text, nullable=False)
    avg_salary = db.Column(db.Integer, nullable=False, default=0)
    user_account = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 表示服务受到许可
    access = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return "{}".format(self.user_account)

    def createInfo(
        self,
        head_photo,
        serviceType,
        live_addr,
        user_id,
        user_account,
        salary,
        timeType,
    ):
        self.user_id = user_id
        self.head_photo = head_photo
        self.user_account = user_account
        self.live_addr = live_addr
        self.timeType = self.TIMETYPE.get(timeType)
        self.serviceType = self.SERVICETYPE.get(serviceType)
        self.avg_salary = self._salary(salary, timeType)

    def activeAcc(self, set=False):
        if set:
            self.access = True
        else:
            self.access = False

    def changeTimeType(self, timeType):
        self.timeType = self.TIMETYPE.get(timeType)

    def _salary(self, salary, timeType, radio=1.5):
        print(salary, timeType, self.TIMETYPE[timeType])
        if self.TIMETYPE[timeType] > 2:
            return salary * radio
        else:
            return salary


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
    ORDERTYPE = {"loading": 1, "received": 2, "start": 4, "done": 8, "pay": 16}
    TIMECELL = {"hour": 1, "day": 2, "month": 4, "year": 8}
    SERVICETYPE = {
        "清洁工": 1,  # 清洁工
        "保姆": 2,  # bao
    }
    id = db.Column(db.String(50), primary_key=True)
    customerId = db.Column(db.String(20), db.ForeignKey("user.account"))
    providerId = db.Column(db.String(20), nullable=False)
    customerTel = db.Column(db.String(15), nullable=True)
    providerTel = db.Column(db.String(15), nullable=True)
    createTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    serviceType = db.Column(db.Integer, nullable=False)
    TimeRange = db.Column(db.Integer, nullable=False)
    TimeCell = db.Column(db.String(10), nullable=False)
    ServiceAddr = db.Column(db.Text, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    preStartTime = db.Column(db.DateTime, nullable=False)
    startTime = db.Column(db.DateTime, nullable=True)
    endTime = db.Column(db.DateTime, nullable=True)
    payTime = db.Column(db.DateTime, nullable=True)
    orderType = db.Column(db.Integer, nullable=False, default=1)

    def create(
        self,
        customerId,
        providerId,
        serviceType,
        TimeRange,
        TimeCell,
        ServiceAddr,
        preStartTime,
        cost,
        customerTel
        # providerTel
    ):
        id = md5()
        key = customerId + str(random.randrange(1, 10000000))
        id.update(key.encode("utf-8"))
        self.id = id.hexdigest()
        self.customerId = customerId
        self.providerId = providerId
        # print(serviceType)
        self.serviceType = serviceType
        self.TimeRange = TimeRange
        self.TimeCell = self.TIMECELL.get(TimeCell)
        self.ServiceAddr = ServiceAddr
        self.orderType = self.ORDERTYPE.get("loading")
        self.preStartTime = preStartTime
        self.salary = cost
        self.providerTel = "12312441241"
        self.customerTel = customerTel

    def actived(self):
        self.orderType = self.ORDERTYPE.get("received")

    def start(self):
        self.startTime = datetime.utcnow
        self.orderType = self.ORDERTYPE.get("start")

    def doing(self):
        self.orderType = self.ORDERTYPE.get("doing")

    def done(self):
        self.endTime = datetime.utcnow
        self.orderType = self.ORDERTYPE.get("done")

    def pay(slef):
        self.payTime = datetime.utcnow
        self.orderType = self.ORDERTYPE.get("pay")
