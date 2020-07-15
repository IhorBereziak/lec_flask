from app import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(150))
    date_create = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, title, text):
        self.title = title
        self.text = text
