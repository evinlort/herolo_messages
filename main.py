from helpers.json import json_dumps
from flask import Flask, request
from flask_api import status
from decorators.validate import validate, validate_token

from functions import *

app = Flask(__name__)


@app.route("/api/auth", methods=['POST'])
def create_token():
    credentials = request.get_json()
    token = get_auth_token(credentials)
    return token


@app.route("/", methods=['GET'])
@validate_token
def hello(**kwargs):
    print("API checker - works for:", kwargs["user"])
    return "Working"


@app.route("/api/write", methods=['POST'])
@validate_token
@validate
def write(user):
    message = request.get_json()
    try:
        save(user, message)
        return "OK", status.HTTP_200_OK
    except Exception as e:
        return f"Not found: {str(e)}", status.HTTP_404_NOT_FOUND


@app.route("/api/all", methods=['GET'])
@validate_token
def all_messages(user):
    messages = get_all(user)
    return json_dumps(messages)


@app.route("/api/unread", methods=['GET'])
@validate_token
def unread(user):
    messages = get_all_unread(user)
    return json_dumps(messages)


@app.route("/api/read", methods=['GET'])
@validate_token
def read(user):
    messages = read_message(user)
    return json_dumps(messages)


@app.route("/api/delete", defaults={"message_id": 0}, methods=['DELETE'])
@app.route("/api/delete/<int:message_id>", methods=['DELETE'])
@validate_token
def delete(user, message_id):
    try:
        delete_message(user, message_id)
        return "OK", status.HTTP_200_OK
    except Exception as e:
        return f"Not found: {str(e)}", status.HTTP_404_NOT_FOUND


@app.route("/api/delete_oldest", methods=['DELETE'])
@validate_token
def delete_oldest(user):
    try:
        delete_old(user)
        return "OK", status.HTTP_200_OK
    except Exception as e:
        return f"Not found: {str(e)}", status.HTTP_404_NOT_FOUND



if __name__ == "__main__":
    '''
    Don't forget to open 5000 (or any other selected) port on firewall
    '''
    app.run(host="0.0.0.0", port=5000, threaded=True)
