from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ams.models import *
from datetime import date ,datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/python_ams'
db = SQLAlchemy(app)


db.create_all()

if __name__ == '__main__':
    app.run(debug=True)