from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import Security
from flask_login import LoginManager
from flask_ckeditor import CKEditor


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = "003d70c345e6136d67b4fb036d0eb77e972dfd72162db05f"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
# admin = Admin(app, name='microblog', template_mode='bootstrap3')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

ckeditor = CKEditor()
ckeditor.init_app(app)

# security = Security(app, user_datastore)

# admin.add_view(ModelView(db.session))
app.app_context().push()

from .routes.index import index_blueprint
from .routes.create_post import post_pages
from .routes.blog import blog_blueprint

app.register_blueprint(post_pages)
app.register_blueprint(index_blueprint)
app.register_blueprint(blog_blueprint)