from api_classes.mongo import Mongo


class Users(Mongo):
    def __init__(self):
        super().__init__()
        self.users = self.db.users
