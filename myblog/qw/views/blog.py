from flask import current_app, Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
from werkzeug.exceptions import abort
from flask_admin.form import Select2Field
from flask_login import current_user, login_required
from flask_admin.contrib.pymongo import ModelView
from datetime import datetime
from qw.db import mongo
from bson.objectid import ObjectId
from qw.forms import PostForm

blog = Blueprint('blog', __name__, template_folder='../templates/blog')


@blog.route('/')
def index():
    articles = mongo.db.blog.find().sort([('_id', -1), ('created_time', -1)])
    return render_template('index.html', articles=articles)


@blog.route('/post', methods=['POST', 'GET'])
@blog.route('/edit/<post_id>', methods=['POST', 'GET'])
@login_required
def post_blog(post_id=None):
    form = PostForm()
    if form.is_submitted():
        if not form.validate():
            return jsonify(str(form.errors))
        posts = {
            'title': form.title.data,
            'content': form.content.data,
            'created_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        if post_id:
            posts['_id'] = post_id
        mongo.db.blog.save(posts)
        return redirect(url_for('blog.index'))
    title = 'Edit' if post_id else 'Edit'
    return render_template('post.html', form=form, title=title)
