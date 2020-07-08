from flask import Blueprint, render_template, request
from app.forms import Posts_Form

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static')

@posts.route('/')
def index():
    return render_template('posts/index.html')

@posts.route('/new/', methods=['POST', 'GET'])
def new_posts():
    form = Posts_Form()
    name = ''
    mail = ''
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']
    return render_template('posts/new_post.html', name=name, mail=mail, form=form)


