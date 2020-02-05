from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from backend import db


class User(db.Model):
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

    def __repr__(self):
        return "<Post %r>" % self.title


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
