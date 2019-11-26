# Maggie Mahoney
#!flask/bin/python
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

users = []                        # the place in memory to store the users instead of a DB

@app.route('/')                   # where to go when going to 127.0.0.1:5000/
def index():
    return 'Hello, world!'        # prints Hello, world! to the screen at the URL above

@app.route('/api/v1.0/addUsers', methods=['POST'])                      # where to go when going to 127.0.0.1:5000/api/v1.0/addUsers
def addUsers():                                                         # the method called when going to the address above
    if not request.json or not 'name' in request.json:                  # if the request isn't in JSON or doesn't have a name
        abort(400)                                                      # error has occurred: ABORT and send 400 code
    elif 'occupation' in request.json and 'age' in request.json:        # if the request has age and occupation
        user = {                                                        # create a user
            "name":request.json["name"],                                # get the name from the request
            "age": request.json["age"],                                 # get the age from the request
            "occupation": request.json["occupation"]                    # get the occupation from the request
        }
    elif 'age' in request.json and not 'occupation' in request.json:    # if the request has age and not occupation
        user = {                                                        # create a user
            "name":request.json["name"],                                # get the name from the request
            "age": request.json["age"]                                  # get the age from the request
        }
    elif 'occupation' in request.json and not 'age' in request.json:    # if the request has occupation and not age
        user = {                                                        # create a user
            "name":request.json["name"],                                # get the name from the request
            "occupation": request.json["occupation"]                    # get the occupation from the request
        }
    else:                                                               # otherwise, the request only has the name
        user = {
            "name": request.json["name"]
        }
    users.append(user)                                              # put the user in the list
    return jsonify({"user": user}), 201                             # return the user in JSON and a Created success code

@app.route('/api/v1.0/getUser/<string:name>', methods=['GET'])      # going to http://127.0.0.1:5000/api/v1.0/getUser/<name>
def getUser(name):                                                  # the method called when going to the URL above
    for user in users:                                              # go through each user in the list
        if user["name"] == name:                                    # check if the current user is the one I am looking for
            return jsonify({'user': user})                          # return the user as a JSON object if I have found it
    return jsonify("User Not Found"), 404                           # the user wasn't found- return a 404 and not found message

@app.route('/api/v1.0/getAllUsers', methods=['GET'])        # use the get request when accessing http://127.0.0.1:5000/api/v1.0/getAllUsers
def getAllUsers():                                          # the method called when accessing the url above
    return jsonify({'users': users})                        # return the list of user as a JSON object

if __name__ == '__main__':                                  # the program starts here
    app.run(debug = True)                                   # run the app
