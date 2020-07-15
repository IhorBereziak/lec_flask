from flask import Blueprint, render_template, request
from app.forms import Posts_Form
from app import db

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static')

from app.models import Post

@posts.route('/')
def index():
    return render_template('posts/index.html')

@posts.route('/new/', methods=['POST', 'GET'])
def new_posts():
    db.create_all()
    form = Posts_Form()
    title = ''
    text = ''
    if request.method == 'GET':
        title = request.args.get('title', '')
        text = request.args.get('text', '')
        if title != '':
            print(dict(request.args))
            for k, v in request.args.items():
                print('k = ', k, 'v = ', v)
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        post = Post(title=title, text=text)
        db.session.add(post)
        db.session.commit()
    return render_template('posts/new_post.html', name=title, mail=text, form=form)

@posts.route('/all/')
def all_posts():
    posts = Post.query.all()
    return render_template('posts/all.html', posts=posts)

