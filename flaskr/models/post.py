class Post:

    def __init__(self, args):
        self.id = args["id"]
        self.auther_id = args["auther_id"]
        self.room_id = args["room_id"]
        self.sent_time = args["sent_time"]
        self.content = args["content"]
