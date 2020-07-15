from wtforms import Form, StringField

class Posts_Form(Form):
    title = StringField('Title')
    text = StringField('Text')


