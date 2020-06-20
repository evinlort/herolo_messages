import json


def json_dumps(message):
    return json.dumps(message, default=str)
