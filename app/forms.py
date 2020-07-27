from wtforms import Form, StringField, SelectField
from app.posts.models import Tag

tags = [(tag.name, tag.name) for tag in Tag.query.all()]
class Posts_Form(Form):
    title = StringField('Title')
    text = StringField('Text')
    tag = SelectField('Tag', choices=tags)

class Tag_Form(Form):
    name = StringField('Name')


