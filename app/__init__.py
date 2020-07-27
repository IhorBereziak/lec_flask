from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# from config import ProdConf

app = Flask(__name__)
# app.config['DEBUG'] = True               #1
# app.config.update(DEBUG=True)            #2
# app.config.from_json('..\config.json')   #3
# app.config.from_object(ProdConf)         #4
app.config.from_object('config.DevConf')  #5

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from .posts.vievs import posts

app.register_blueprint(posts, url_prefix='/posts')

from app import vievs