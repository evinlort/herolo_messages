from app.api_classes.messages import Messages


class GetAllMessages(Messages):
    def __init__(self):
        super().__init__()

    def get(self, user):
        results = list(self.messages.find({"receiver": user}))
        for result in results:
            if "creation_date" in result:
                result["creation_date"] = str(result["creation_date"])
            del result["_id"]
        return results
