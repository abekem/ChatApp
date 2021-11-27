from flask import Flask
from mongoengine import connect

app = Flask(__name__)
app.config.from_object('chatapp.config')

# connect(
#     db='mongo',
#     port=27017,
#     username='root',
#     password='password',
#     authentication_source='admin'
# )
connect(host="mongodb://root:password@mongo:27017/mongo?authSource=admin")
# client = MongoClient('mongo', port=27017)
# client['admin'].authenticate("root", "password")
# db = client.test_db

import chatapp.views
