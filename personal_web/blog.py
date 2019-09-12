from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from personal_web.auth import login_required
from personal_web.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    categorys = db.execute(
        'SELECT DISTINCT category FROM post'
    ).fetchall()
    post_myprofile = db.execute(
        'SELECT title, body FROM post'
        " WHERE category = 'myprofile'"
    ).fetchall()
    post_project = db.execute(
        'SELECT title, body FROM post'
        " WHERE category = 'project'"
    ).fetchall()
    post_studying = db.execute(
        'SELECT title, body FROM post'
        " WHERE category = 'studying'"
    ).fetchall()
    post_daily = db.execute(
        'SELECT title, body FROM post'
        " WHERE category = 'daily'"
    ).fetchall()

    return render_template('blog/index.html', categorys=categorys, post_myprofile=post_myprofile, post_project=post_project, post_studying=post_studying, post_daily=post_daily)

@bp.route('/myprofile')
def myprofile():
    return render_template('blog/myprofile.html')

@bp.route('/project')
def project():
    return render_template('blog/project.html')

@bp.route('/studying')
def studying():
    return render_template('blog/studying.html')

@bp.route('/daily')
def daily():
    return render_template('blog/daily.html')
'''
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
'''

'''
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
'''


'''
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
'''