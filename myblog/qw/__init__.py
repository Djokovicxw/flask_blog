from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from qw.db import init_extension
from qw.views import blog, auth
import config


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config)
    bootstrap = Bootstrap(app)
    app.register_blueprint(blog.blog)
    app.register_blueprint(auth.auth)
    app.config["MONGO_URI"] = 'mongodb://127.0.0.1:27017/blog'
    app.config["SECRET_KEY"] = "qiangweijuanjuan"
    init_extension(app)
    return app
