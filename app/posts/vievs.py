from flask import Blueprint, render_template, request
from app.forms import Posts_Form, Tag_Form
from app import db

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static')

from app.posts.models import Post, Tag


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
        tag_name = request.form['tag']

        tag = Tag.query.filter_by(name=tag_name).first()
        post = Post(title=title, text=text)

        post.tag.append(tag)
        db.session.add(post)
        db.session.commit()
    return render_template('posts/new_post.html', name=title, mail=text, form=form)


@posts.route('/all/')
def all_posts():
    posts = Post.query.all()
    return render_template('posts/all.html', posts=posts)


@posts.route('/new-tag/', methods=['POST', 'GET'])
def new_tag():
    form = Tag_Form()
    if request.method == 'POST':
        name = request.form['name']
        tag = Tag(name=name)
        db.session.add(tag)
        db.session.commit()
    tags = Tag.query.all()
    return render_template('posts/new_tag.html', form=form, tags=tags)


@posts.route('/edit/<post_name>', methods=['POST', 'GET'])
def edit_post(post_name):
    post = Post.query.filter_by(title=post_name).first()
    form = Posts_Form(title=post.title, text=post.text)
    if request.method == 'POST':
        post.title = request.form['title']
        post.text = request.form['text']
        tag_name = request.form['tag']

        tag = Tag.query.filter_by(name=tag_name).first()

        post.tag.append(tag)
        db.session.add(post)
        db.session.commit()
        post = Post.query.filter_by(title=post_name).first()
    return render_template('posts/edit_post.html', form=form, post=post)
