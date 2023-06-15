from inspect import Attribute
from ssl import SSLSession
from PortfolioApp import db, app, login_manager
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from flask_admin.contrib import sqla
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask import session, abort
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)

admin = Admin(app, name="test", template_mode='bootstrap3')
admin.add_view(SecureModelView(Post, db.session))

# user_datastore = SQLAlchemyUserDatastore(db, Post)
# security = Security(app, user_datastore)