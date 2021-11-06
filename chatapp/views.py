from flask import request, redirect, url_for, render_template, flash
from chatapp import app
from chatapp.models.user import User
from chatapp.models.post import Post
from chatapp.models.room import Room
from chatapp.models.seeds import seed_posts
from time import time
from datetime import datetime

posts = seed_posts()


@app.route('/')
def show_posts():
    # posts = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_posts.html', posts=posts)


@app.route('/add', methods=['POST'])
def add_post():
    now = datetime.fromtimestamp(time()).strftime('%Y/%m/%d %H:%M:%S')
    post = Post({"id": 2, "auther_id": 1, "room_id": 1, "sent_time": now, "content": request.form['content']})
    posts.append(post)
    return redirect(url_for('show_posts'))
