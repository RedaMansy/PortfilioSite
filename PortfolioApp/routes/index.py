# from PortfolioApp import app
from flask import render_template, flash, session, Blueprint, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from PortfolioApp.forms import LoginForm
from PortfolioApp.models import User
from flask_login import login_user, current_user, logout_user, login_required

index_blueprint = Blueprint("index", __name__)

@index_blueprint.route('/')
@index_blueprint.route('/home', methods=["GET", "POST"])

def home():
    return render_template('index.html')

@login_required
@index_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('You are now logged in.')
            session["logged_in"] = True
            return redirect(url_for('admin.index'))
        flash('Invalid username or password.')

        return render_template('login.html', form=form)

    return render_template('login.html', title='Login', form=form)

@index_blueprint.route('/')
def index():
    return render_template('index.html')

@index_blueprint.route("/logout")
def logout():
    session.clear()
    return redirect('/')
