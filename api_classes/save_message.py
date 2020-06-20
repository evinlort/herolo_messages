from api_classes.messages import Messages
from datetime import datetime
import pymongo


class SaveMessage(Messages):
    def __init__(self):
        super().__init__()
        self.receiver = ""
        self.sender = ""

    def write(self, message: dict) -> str:
        self.receiver = message["receiver"]
        self.sender = message["sender"]
        message["id"] = self.generate_inc_id()
        message["creation_date"] = datetime.now()
        message["was_read"] = False
        inserted = self.messages.insert_one(message).inserted_id
        return str(inserted)

    def generate_inc_id(self):
        last_id = self.messages.find({}, {"id": 1,"_id": 0}).sort("id", pymongo.DESCENDING).limit(1)[0]

        if len(last_id) == 0:
            last_id = 1
        else:
            last_id = last_id["id"] + 1
        return last_id
