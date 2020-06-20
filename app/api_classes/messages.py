from app.api_classes.mongo import Mongo


class Messages(Mongo):
    def __init__(self):
        super().__init__()
        self.messages = self.db.messages
