from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('chatapp.config')

client = MongoClient('mongo', 27017)
client['admin'].authenticate("root", "password")
db = client.test_db

import chatapp.views
