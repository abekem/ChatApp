from .user import User
from .room import Room
from .post import Post
from chatapp import db


def seed_users():
    users = db.user_collection
    users.drop()
    users.insert({"id": 1, "name": "abe", "password": "a", "friends": [2, 3, 5]})
    users.insert({"id": 2, "name": "ken", "password": "a", "friends": [1, 4, 5]})
    users.insert({"id": 3, "name": "taro", "password": "a", "friends": [1, 5, 6]})
    users.insert({"id": 4, "name": "sio", "password": "a", "friends": [2, 6]})
    users.insert({"id": 5, "name": "yama", "password": "a", "friends": [1, 2, 3, 6]})
    users.insert({"id": 6, "name": "jun", "password": "a", "friends": [3, 4, 5]})
    return users


def seed_rooms():
    rooms = db.room_collection
    rooms.drop()
    rooms.insert({"id": 1, "participants": [1, 5]})
    return rooms


def seed_posts():
    posts = db.post_collection
    posts.drop()
    posts.insert({"id": 1, "auther_id": 1, "room_id": 1, "sent_time": 1, "content": "Hello."})
    return posts
