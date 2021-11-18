class User:

    def __init__(self, args):
        self.id = args["id"]
        self.name = args["name"]
        self.email = args["email"]
        self.password = args["password"]
        self.friends = args["friends"]
