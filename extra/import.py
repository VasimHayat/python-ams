import csv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/python_ams'
db = SQLAlchemy(app)


#Admin User
class EOAdminUser(db.Model):
    __tablename__ = 'eoadminuser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=True)


#Session class
class EOGrade(db.Model):
    __tablename__ = 'eograde'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    acadmic_year = db.Column(db.Integer, nullable=False, default='2021')
    info = db.Column(db.Text, nullable=False)
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
    inactive = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    
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


# Import grade data to db
def importGrade():
        f1 = open("_grade.csv")
        gradeReader = csv.reader(f1)
        i=0
        for id,name,acadmic_year,info in gradeReader:
            i = i+1
            if i==1: 
             continue
            eograde = EOGrade(id=id,name=name,acadmic_year=acadmic_year,info=info)
            db.session.add(eograde)
        db.session.commit()
     
 
 
 # Import Student data to db
def importStudent():
        f1 = open("_student.csv")
        studentReader = csv.reader(f1)
        i=0
        for id,name,email,gender,dob,password,eograde_id in studentReader:
            i = i+1
            if i==1: 
             continue
            eoStudent = EOStudent(id =id,name=name,email=email,gender=gender,dob=dob,password=password,eograde_id=eograde_id)
            db.session.add(eoStudent)
        db.session.commit()
     
# Import admin data to db
def importAdminUser():
        f1 = open("_admin.csv")
        adminReader = csv.reader(f1)
        i=0
        for id, username,email,password in adminReader:
            i = i+1
            if i==1: 
             continue
            adminUser = EOAdminUser(id = id,username=username,email=email,password=password)
            db.session.add(adminUser)
        db.session.commit()
             
    

def main():    
     #importAdminUser()
     #importGrade()
     importStudent()

if __name__ == "__main__":
    db.create_all()
    main()
