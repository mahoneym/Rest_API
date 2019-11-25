# Rest_API
Maggie Mahoney
Project 4 

This project implements a Rest API POST method using Python2 and Flask. I developed the program on a Kali Linux VirtualBox, so all commands shown below are for a Linux terminal. I used a virtual environment called HelloWorld.

The project can be run by navigating into the HelloWorld file. The test webpage can be seen by running: 'python Hello.py' in a terminal window and navigating to http://127.0.0.1:5000/ in the web browser. "Hello, world!" should appear on the screen.

To use the API functionality, run 'python Hello.py' in a terminal window. Open another terminal window and run the command:
  'curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Test","age":"100","occupation":"programmer"}' http://127.0.0.1/api/v1.0/addUsers'
 to add a user. When the command is successful, the terminal will show a HTTP/1.0 201 response. Note: using the wrong quotation marks will cause parse errors in the program and will cause the program to fail.

After the user has been added, you can get the information for a single user by running:
  'curl -i http://127.0.0.1/api/v1.0/getUser/Test'
When this command is successful, there will be a 200 response and the user whose name was requested in the URL will be printed.

Finally, the API has a functionality for listing out all the users. This can be recreated by creating multiple users using the command from above then using
      'curl -i http://127.0.0.1:5000/api/v1.0/getAllUsers'
This command should return a HTTP/1.0 200 OK response and print all the users which have been added to the list in memory. I have included screenshots of my terminals when I successfully ran the program.
