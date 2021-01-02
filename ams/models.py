 
from datetime import date ,datetime
from ams import db ,login_manager 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return EOAdminUser.query.get(int(user_id))


#Admin User
class EOAdminUser(db.Model,UserMixin):
    __tablename__ = 'eoadminuser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


#Session class
class EOGrade(db.Model):
    __tablename__ = 'eograde'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    acadmic_year = db.Column(db.Integer, nullable=False, default='2021')
    info = db.Column(db.Text, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=True)
    #eostudent_list = db.relationship("EOStudent", backref="eoclass", lazy=True)

    #Student


class EOStudent(db.Model):
    __tablename__ = 'eostudent'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120), nullable=False,default='NA')
    dob = db.Column(db.Date(), nullable=True, default='2020-01-01')
    password = db.Column(db.String(60), nullable=False)
    unique_face_byte = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(20), nullable=False, default='default.jpg')
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=True)
    
    eograde_id = db.Column(db.Integer, db.ForeignKey(
        "eograde.id"), nullable=False)
    #eoattendance_list = db.relationship("EOAttendance", backref="eostudent", lazy=True)


class EOAttendance (db.Model):
    __tablename__ = 'eoattendance'

    id = db.Column(db.Integer, primary_key=True)
    busi_date = db.Column(db.Date(), nullable=False, default=date.today())
    eostudent_id = db.Column(db.Integer, db.ForeignKey(
        "eostudent.id"), nullable=False)
    eograde_id = db.Column(db.Integer, db.ForeignKey(
        "eograde.id"), nullable=False)
    is_present = db.Column(db.Boolean, nullable=False, default=False)
    on_leave = db.Column(db.Boolean, nullable=False, default=False)
