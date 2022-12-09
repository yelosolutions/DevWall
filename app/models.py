from app import db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.Text)
    profile_pic = db.Column(db.String(255))

    def __repr__(self):
        return '<User %r>' % self.username