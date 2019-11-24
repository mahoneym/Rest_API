# Rest_API
Project 4 for Networking

This project implements a Rest API POST method using Python2 and Flask. I developed the program on a Kali Linux VirtualBox and used a virtual environment. The virtual environment I set up was called HelloWorld.

The project can be run by navigating into HelloWorld. The test webpage for the virtual environment can be seen by running: 'python Hello.py' in a terminal window and navigating to http://127.0.0.1:5000/ in the web browser. "Hello, world!" should appear on the screen. 

To use the API functionality, once again, run 'python Hello.py' in a terminal window. Another terminal window will be needed to test the API. To add a user, run the command:
  'curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Test","age":"100","occupation":"programmer"}' http://127.0.0.1/api/v1.0/addUsers'
When the command is successful, the terminal will show a HTTP/1.0 201 response. Note: using the wrong quotation marks will cause parse errors in the program and will cause it to fail.

After the user has been added, you can get the information for a single user by running:
  'curl -i http://127.0.0.1/api/v1.0/getUser/Test'
When this command is sucessful, there will be a 200 response and the user whose name was requested will be printed. I have included screenshots of my terminals when I successfully ran the program. 
