from wtforms import Form, StringField

class Posts_Form(Form):
    name = StringField('name')
    mail = StringField('mail')


