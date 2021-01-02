from flask import render_template, url_for, flash, redirect, request, Blueprint,session
from flask_login import login_user, logout_user, current_user, login_required

# from ams import app
from ams.forms import RegistrationForm, LoginForm
from ams.models import EOAdminUser,EOStudent
from ams.img_capture import capture_video
from ams import db


users = Blueprint("users", __name__)


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

 
@users.route("/home")
@login_required
def home():      
    eoStudent = EOStudent.query.get(session['id'])
    return render_template('home.html', user=eoStudent)


@users.route("/profile")
@login_required
def profile():
    return render_template('profile.html', title='Profile')

@users.route("/face_config")
@login_required
def face_config():
    student = EOStudent.query.get(session['id'])
    file_Path = capture_video(student.name)
    student = EOStudent.query.get(student.id)
    if file_Path:
        student.unique_face_byte =file_Path
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("users.home"))
    return render_template('home.html', user=student)


@users.route("/attandence")
@login_required
def attandence():
    student = EOStudent.query.get(session['id'])
    file_Path = capture_video(student.name)
    student = EOStudent.query.get(student.id)
    if file_Path:
        student.unique_face_byte =file_Path
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("users.home"))
    return render_template('home.html', user=student)


# @users.route("/account", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


# @users.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)
