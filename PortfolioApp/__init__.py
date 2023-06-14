from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = "003d70c345e6136d67b4fb036d0eb77e972dfd72162db05f"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# admin = Admin(app, name='microblog', template_mode='bootstrap3')

db = SQLAlchemy(app)

# admin.add_view(ModelView(db.session))
app.app_context().push()

from .routes.index import index_blueprint
from .routes.create_post import post_pages
from .routes.blog import blog_blueprint

app.register_blueprint(post_pages)
app.register_blueprint(index_blueprint)
app.register_blueprint(blog_blueprint)

