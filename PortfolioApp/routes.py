from PortfolioApp import app
from flask import render_template, Blueprint, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email



# app = Blueprint("posts", __name__)



@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.get("/post/<string:title>")
def display_post(title: str):
    return "Display post page"

@app.route('/create_post', methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        return redirect(url_for(".display_post", title=title))
    return render_template("new_post.html")
