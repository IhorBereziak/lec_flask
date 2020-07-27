from app import db
from datetime import datetime

post_tag = db.Table('post_tag',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(150))
    date_create = db.Column(db.DateTime, default=datetime.now)

    tag = db.relationship('Tag', secondary=post_tag, backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, text):
        self.title = title
        self.text = text

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

