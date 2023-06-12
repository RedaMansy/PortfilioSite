# from PortfolioApp import app
from flask import render_template, Blueprint, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

index_blueprint = Blueprint("index", __name__)

@index_blueprint.route('/')
@index_blueprint.route('/home', methods=["GET", "POST"])

def home():
    return render_template('index.html')
