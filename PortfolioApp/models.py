from PortfolioApp import db, app
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)

admin = Admin(app, name="test", template_mode='bootstrap3')
admin.add_view(ModelView(Post, db.session))