from flask import Blueprint, redirect, url_for, render_template, request
from flask import current_app
from sqlmodel import Session, select
from PortfolioApp.models import Post


post_pages = Blueprint("posts", __name__)


@post_pages.get("/post/<string:title>")
def display_post(title: str):
    return "Display post page"

@post_pages.route('/create_post', methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        with Session(current_app.engine) as session:
            session.add(Post(title=title, content=content))
            session.commit()

        return redirect(url_for(".display_post", title=title))
    return render_template("new_post.html")