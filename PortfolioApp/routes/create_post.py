from flask import Blueprint, redirect, url_for, render_template, request

post_pages = Blueprint("posts", __name__)


@post_pages.get("/post/<string:title>")
def display_post(title: str):
    return "Display post page"

@post_pages.route('/create_post', methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        return redirect(url_for(".display_post", title=title))
    return render_template("new_post.html")