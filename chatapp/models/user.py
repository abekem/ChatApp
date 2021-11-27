from mongoengine.document import Document
from mongoengine import fields


class User(Document):
    id = fields.IntField(primary_key=True)
    name = fields.StringField()
    email = fields.StringField()
    # fields.EmailField()
    password = fields.StringField()
    # friends = args["friends"]
