from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db = SQLAlchemy(app)

app.app_context().push()

from .routes.index import index_blueprint
from .routes.create_post import post_pages
from .routes.blog import blog_blueprint

app.register_blueprint(post_pages)
app.register_blueprint(index_blueprint)
app.register_blueprint(blog_blueprint)

