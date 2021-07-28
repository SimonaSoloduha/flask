from flask_login import UserMixin
from flask_security import RoleMixin

from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(100))
    roles = db.Column(db.String(100), default='user')

    def __init__(self, name, email, password, roles):
        self.name = name
        self.email = email
        self.password = password
        self.roles = roles

    def __repr__(self):
        return '<User %r>' % self.name


# export FLASK_APP=project
# export FLASK_DEBUG=1
