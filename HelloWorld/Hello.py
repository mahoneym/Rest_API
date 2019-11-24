#!flask/bin/python
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

users = []

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/v1.0/addUsers', methods=['POST'])
def addUsers():
    if not request.json: #or not 'name' in request.json:
        abort(400)
    user = {
        "name":request.json["name"],
        "age": request.json["age"],
        "occupation": request.json["occupation"]
    }
    users.append(user)
    return jsonify({'user': user}), 201

if __name__ == '__main__':
    app.run(debug = True)
