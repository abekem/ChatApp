from mongoengine.document import Document
from mongoengine import fields


class Room(Document):
    id = fields.IntField(primary_key=True)
    # name = fields.StringField()
    # participants = args["participants"]
