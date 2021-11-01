from models.user import User
from models.room import Room
from models.post import Post


def seed_users():
    users = []
    users.append(User({"id": 1, "name": "abe", "password": "a", "friends": [2, 3, 5]}))
    users.append(User({"id": 2, "name": "ken", "password": "a", "friends": [1, 4, 5]}))
    users.append(User({"id": 3, "name": "taro", "password": "a", "friends": [1, 5, 6]}))
    users.append(User({"id": 4, "name": "sio", "password": "a", "friends": [2, 6]}))
    users.append(User({"id": 5, "name": "yama", "password": "a", "friends": [1, 2, 3, 6]}))
    users.append(User({"id": 6, "name": "jun", "password": "a", "friends": [3, 4, 5]}))
    return users


def seed_rooms():
    rooms = []
    rooms.append(Room({"id": 1, "participants": [1, 5]}))
    return rooms


def seed_posts():
    posts = []
    posts.append(Post({"id": 1, "auther_id": 1, "room_id": 1, "sent_time": 1, "content": "Hello."}))
    return posts
