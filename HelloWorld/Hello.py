#!flask/bin/python
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

users = []                        # the place in memory to store the users instead of a DB

@app.route('/')                   # where to go when going to 127.0.0.1:5000/
def index():
    return 'Hello, world!'        # prints Hello, world! to the screen

@app.route('/api/v1.0/addUsers', methods=['POST'])          # where to go when going to 127.0.0.1:5000/api/v1.0/addUsers
def addUsers():                                             # the method called when going to the address above
    if not request.json or not 'name' in request.json:
        abort(400)                                          # error has occurred: ABORT
    user = {                                                # create a user
        "name":request.json["name"],                        # get the name from the request
        "age": request.json["age"],                         # get the age from the request
        "occupation": request.json["occupation"]            # get the occupation from the request
    }
    users.append(user)                                      # put the user in the list
    return jsonify({"user": user}), 201                     # return the user in JSON and a success code

@app.route('/api/v1.0/getUser/<string:name>', methods=['GET'])
def getUser(name):
    for user in users:
        if user["name"] == name:
            return jsonify({'users': user})

if __name__ == '__main__':                                  # the program starts here
    app.run(debug = True)                                   # run the app
