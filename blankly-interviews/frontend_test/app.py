import json

import flask
from flask import Flask
from flask_cors import CORS
import hashlib

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

messages = [
    {"encrypted_message": "3d7a3babee7105644c53d8d66b95ba2094c6c0433dd7b000bf0d4007f47d8e25",
     "original_message": "Blankly", "timestamp": 1208811506},
    {"encrypted_message": "b696d75511dc16f2b52563e3113a498311a79866f4672862197aa9a8c5c0da12",
        "original_message": "Finance", "timestamp": 1668887702},
]


@app.route("/get_one", methods=["GET"])
def get_one():
    return json.dumps(messages[0])


@app.route("/get_x", methods=["POST"])
def get_x():
    global messages
    req = flask.request.json
    if "num" not in req and type(req['num']) != int:
        return "Invalid post request", 400
    if req.num > len(messages):
        return "Too large of a request", 300
    return json.dumps(messages[:int(req['num'])])


@app.route("/get", methods=["GET"])
def get_messages():
    global messages
    return json.dumps(messages)


@app.route("/add", methods=["POST"])
def add_message():
    global messages
    req = flask.request.json
    if "message" not in req:
        return "Message not found", 400
    if "timestamp" not in req:
        return "Timestamp not found", 400
    elif not isinstance(req['timestamp'], int):
        return "Timestamp must be an integer"
    #
    m = hashlib.sha256()
    m.update(req['message'].encode('utf-8'))
    sha = m.hexdigest()
    messages.append({"encrypted_message": sha, "original_message": req['message'], "timestamp": int(req['timestamp'])})
    return "success"


# ip address
if __name__ == '__main__':
    app.run()

