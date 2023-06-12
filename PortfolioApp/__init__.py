from flask import Flask

from .routes.index import index_blueprint
from .routes.create_post import post_pages
from .routes.blog import blog_blueprint


app = Flask(__name__)

app.register_blueprint(post_pages)
app.register_blueprint(index_blueprint)
app.register_blueprint(blog_blueprint)

