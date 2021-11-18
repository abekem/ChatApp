from flask import request, redirect, url_for, render_template, flash, session
from chatapp import app, db
from chatapp.models.user import User
from chatapp.models.post import Post
from chatapp.models.room import Room
from chatapp.models.seeds import seed_posts, seed_users
from time import time
from datetime import datetime

posts = seed_posts()
users = seed_users()


@app.route('/')
def show_posts():
    # posts = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_posts.html', posts=posts.find(), users=users)


@app.route('/add', methods=['POST'])
def add_post():
    if 'user_id' in session:
        auther_id = session['user_id']
        now = datetime.fromtimestamp(time()).strftime('%Y/%m/%d %H:%M:%S')
        post = {"id": posts.count() + 1, "auther_id": auther_id, "room_id": 1, "sent_time": now, "content": request.form['content']}
        posts.insert(post)
        flash('New entry was successfully posted')
    else:
        flash('You must log in')
    return redirect(url_for('show_posts'))


@app.route('/users/')
def user_list():
    return 'list users'


@app.route('/users/<int:user_id>/')
def user_detail(user_id):
    return 'detail user' + str(user_id)


@app.route('/users/<int:user_id>/edit/', methods=['GET', 'POST'])
def user_edit(user_id):
    return 'edit user ' + str(user_id)


@app.route('/users/create/', methods=['GET', 'POST'])
def user_create():
    return 'create a new user'


@app.route('/users/<int:user_id>/delete/', methods=['DELETE'])
def user_delete(user_id):
    return NotImplementedError('DELETE')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = users.find_one({"email": request.form['email']})
        if user['password'] == request.form['password']:
            session['user_id'] = user['id']
            flash('You were logged in')
            return redirect(url_for('show_posts'))
        else:
            flash('Invalid email or password')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You were logged out')
    return redirect(url_for('show_posts'))
