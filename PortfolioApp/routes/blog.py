from flask import Blueprint, redirect, url_for, render_template, request

blog_blueprint = Blueprint("blog", __name__)

@blog_blueprint.route("/blog", methods=["GET", "POST"])
def blog():
    return render_template("newblog.html")