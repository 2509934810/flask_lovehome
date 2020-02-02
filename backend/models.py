from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from backend import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    # auth = db.relationship("Auth", backref="user")
    
    def __repr__(self):
        return '<Post %r>' % self.title

# class Auth(db.Model):
#     auth_token = db.Column(db.String(30), unique=True)
#     level = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
