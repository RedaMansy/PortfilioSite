from PortfolioApp import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)

