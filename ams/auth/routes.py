from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required

# from ams import app
from ams.forms import RegistrationForm, LoginForm
from ams.models import EOAdminUser


auth = Blueprint("auth", __name__) 


@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@auth.route("/")
def index(): 
    return render_template('index.html', title='AMS')


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = EOAdminUser.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("users.home"))
        else:
              flash('Please check your login details and try again.','danger') 
    return render_template("login.html", title="Login", form=form)


@auth.route("/logout")
def logout():  
    logout_user() 
    return redirect(url_for('auth.index'))

@auth.route("/signup")
def signup_post(): 
    return render_template('signup.html', title='Signup')
