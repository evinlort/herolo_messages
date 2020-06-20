import pymongo

from api_classes.messages import Messages


class DeleteMessage(Messages):
    def __init__(self):
        super().__init__()

    def delete_oldest(self, user):
        oldest_id = self.get_lowest_id(user)
        if self.messages.delete_one({
            "$or": [
                {"receiver": user},
                {"sender": user}
            ],
            "id": oldest_id
        }).deleted_count != 1:
            raise Exception("Error with delete")
        return "OK"

    def get_lowest_id(self, user):
        return self.messages.find({
            "$or": [
                {"receiver": user},
                {"sender": user}
            ],
            "id" : {"$exists": True}
        }).sort("id", pymongo.ASCENDING).limit(1)[0]["id"]

    def delete(self, user, message_id: int):
        if message_id == 0:
            raise Exception("No message ID, if you want delete oldest message, use api/delete_oldest")
        message = self.get_message_by_id(message_id)
        if not message:
            raise Exception("Wrong message ID")
        if self.messages.delete_one({
            "$or": [
                {"receiver": user},
                {"sender": user}
            ],
            "id": message_id
        }).deleted_count != 1:
            raise Exception("Error with delete")
        return "OK"

    def get_message_by_id(self, mess_id):
        return self.messages.find_one({"id": mess_id})
