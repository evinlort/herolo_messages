from pymongo import MongoClient


class Mongo:
    def __init__(self):
        client = MongoClient(
            "mongodb+srv://evgeny:Zh0pAn123@cluster0-g6kar.mongodb.net/herolo_messages?retryWrites=true&w=majority")
        self.db = client.herolo_messages
