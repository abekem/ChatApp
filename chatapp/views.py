from flask import request, redirect, url_for, render_template, flash, session
from chatapp import app, db
# from chatapp.models.user import User
# from chatapp.models.post import Post
# from chatapp.models.room import Room
from chatapp.models.seeds import seed_posts, seed_users, seed_rooms
from time import time
from datetime import datetime

posts = seed_posts()
users = seed_users()
rooms = seed_rooms()


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
    return render_template('user/list.html', users=users.find())


@app.route('/users/<int:user_id>/')
def user_detail(user_id):
    return 'detail user' + str(user_id)


@app.route('/users/<int:user_id>/edit/', methods=['GET', 'POST'])
def user_edit(user_id):
    return 'edit user ' + str(user_id)


@app.route('/users/create/', methods=['GET', 'POST'])
def user_create():
    if request.method == 'POST':
        user = {"id": users.count() + 1,
                "name": request.form['name'], 
                "email": request.form['email'],
                "password": request.form['password']}
        users.insert(user)
        return redirect(url_for('user_list'))
    return render_template('user/edit.html')


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


@app.route('/rooms/')
def room_list():
    # pass
    # セッションユーザが所属している部屋のリスト
    return render_template('room/list.html', rooms=rooms.find())


@app.route('/rooms/create/')
def room_create():
    # 部屋の作成
    # pass
    room = {"id": rooms.count() + 1,
            "participants": []}
    rooms.insert(room)
    return redirect(url_for('room_list'))


@app.route('/rooms/<int:room_id>/')
def show_posts_in_room(room_id):
    return render_template('room/show_posts.html', posts=posts.find({"room_id": room_id}), users=users, room_id=room_id)


@app.route('/rooms/<int:room_id>/add', methods=['POST'])
def add_post_in_room(room_id):
    if 'user_id' in session:
        auther_id = session['user_id']
        now = datetime.fromtimestamp(time()).strftime('%Y/%m/%d %H:%M:%S')
        post = {"id": posts.count() + 1, "auther_id": auther_id, "room_id": room_id, "sent_time": now, "content": request.form['content']}
        posts.insert(post)
        flash('New entry was successfully posted')
    else:
        flash('You must log in')
    return redirect(url_for('show_posts_in_room', room_id=room_id))
