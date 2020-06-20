from api_classes.messages import Messages


class Read(Messages):
    def __init__(self):
        super().__init__()

    def read(self, user):
        result = self.messages.find_one({"receiver": user, "was_read": False}, sort=[("creation_date", 1)])
        if result:
            updated = self.messages.update_one({"_id": result["_id"]}, {"$set": {"was_read": True}})
            if updated.modified_count != 1:
                return "Something wrong with update"
            del result["_id"]
            del result["was_read"]
            return result
        return list()
