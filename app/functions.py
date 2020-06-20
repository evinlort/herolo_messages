from api_classes.authenticate import Authenticate
from api_classes.delete_message import DeleteMessage
from api_classes.get_all import GetAllMessages
from api_classes.get_all_unread import GetAllUnreadMessages
from api_classes.read import Read
from api_classes.save_message import SaveMessage


def get_auth_token(credentials):
    return Authenticate(credentials).get_auth_token()


def save(user, message):
    message["sender"] = user
    return SaveMessage().write(message)


def delete_message(user, message_id):
    return DeleteMessage().delete(user, message_id)


def delete_old(user):
    return DeleteMessage().delete_oldest(user)


def get_all(user):
    return GetAllMessages().get(user)


def get_all_unread(user):
    return GetAllUnreadMessages().get(user)


def read_message(user):
    return Read().read(user)
