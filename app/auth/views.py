from flask import render_template,flash, request,redirect, url_for
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from ..email import mail_message
from app.auth import auth
from app.models import User

@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid')
    return render_template('auth/login.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/signup', methods = ["POST","GET"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,
                    email = form.email.data,
                    password = form.password.data)
        user.save_u()
        mail_message("Welcome to My-Blog","email/welcome",user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', registration_form = form)