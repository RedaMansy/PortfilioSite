from flask import flash, Blueprint, redirect, url_for, render_template, request
from flask import current_app
from sqlmodel import Session, select
from PortfolioApp import db
from PortfolioApp.models import Post
from PortfolioApp.forms import PostForm
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from flask_security.utils import encrypt_password


post_pages = Blueprint("posts", __name__)



# @post_pages.get("/post/<string:title>")
@post_pages.route("/blog", methods=["GET", "POST"])
def display_post():
    posts = Post.query.all()
    print(posts)
    return render_template("blog.html", posts=posts)

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




# @security.context_processor
# def security_context_processor():
#     return dict(
#         admin_base_template=admin.base_template,
#         admin_view=admin.index_view,
#         h=admin_helpers,
#         get_url=url_for
#     )