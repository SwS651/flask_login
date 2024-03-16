from flask_login import UserMixin
from app.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin,db.Model):
    # __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    StaffID = db.Column(db.String,unique = True)
    StaffName = db.Column(db.String(50))
    Email = db.Column(db.String(50), unique=True, nullable=False)
    Password = db.Column(db.String(80), nullable=False)
    Role = db.Column(db.String(10))

    def __init__(self, StaffID, StaffName, Email,Password,Role):
        self.StaffID = StaffID
        self.StaffName = StaffName
        self.Email = Email
        self.Password = Password
        self.active = False
        self.Role = "Staff"

    def set_password(self, password):
        self.Password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Password, password)