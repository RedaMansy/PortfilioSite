from flask import flash, Blueprint, redirect, url_for, render_template, request
from flask import current_app
from sqlmodel import Session, select
from PortfolioApp import db
from PortfolioApp.models import Post
from PortfolioApp.forms import PostForm


post_pages = Blueprint("posts", __name__)


@post_pages.get("/post/<string:title>")
def display_post(title: str):
    return "Display post page"

@post_pages.route('/create_post', methods=["GET", "POST"])
def create_post():
    form = PostForm()
    if request.method == "POST":
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash("Post submitted!")

        return redirect(url_for("posts.create_post"))

    return render_template("new_post.html", form=form)