from app.api_classes.users import Users
import jwt
import datetime
from app.helpers.configs import key


class Authenticate(Users):
    def __init__(self, credentials):
        super().__init__()
        self.username = credentials["username"]
        self.password = credentials["password"]

    def get_auth_token(self):
        user = self.users.find_one({"username": self.username, "password": self.password})
        if not user:
            return "User not found"
        del user["_id"]
        extended_user = {**user,
                         **{"exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=15)}}
        token = jwt.encode(extended_user, key, algorithm="HS256")
        return token.decode("utf-8")
