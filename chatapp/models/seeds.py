from .user import User
from .room import Room
from .post import Post
from datetime import datetime


def seed_users():
    if User.objects.count() == 0:
        User(id=1, name='abe', email='abe@example.com', password='a').save()
        User(id=2, name='ken', email='ken@example.com', password='a').save()
        User(id=3, name='taro', email='taro@example.com', password='a').save()
        User(id=4, name='sio', email='sio@example.com', password='a').save()
        User(id=5, name='yama', email='yama@example.com', password='a').save()
        User(id=6, name='jun', email='jun@example.com', password='a').save()


def seed_rooms():
    if Room.objects.count() == 0:
        Room(id=1).save()
        Room(id=2).save()


def seed_posts():
    if Post.objects.count() == 0:
        Post(id=1, auther_id=1, room_id=1, sent_time=datetime.now(), content='Hello.').save()
