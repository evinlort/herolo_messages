from pymongo import MongoClient


class Mongo:
    def __init__(self):
        client = MongoClient("localhost")
        self.db = client.herolo_messages
