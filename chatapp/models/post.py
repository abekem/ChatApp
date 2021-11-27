from mongoengine.document import Document
from mongoengine import fields
from datetime import datetime


class Post(Document):
    id = fields.IntField(primary_key=True)
    auther_id = fields.IntField()
    room_id = fields.IntField()
    sent_time = fields.DateTimeField(default=datetime.now())
    content = fields.StringField()
