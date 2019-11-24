# Rest_API
Project 4 for Networking

This project implements a Rest API POST method using Python2 and Flask. I developed the program on a Kali Linux VirtualBox and used a virtual environment. The virtual environment I set up is called HelloWorld. The project can be run by starting HelloWorld, which is done on Linux by running 'source HelloWorld/bin/activate' within the Rest_API folder. 

The test webpage for the virtual environment can be seen by running: 'python Hello.py' within the virtual environment and navigating to http://127.0.0.1:5000/ in a web browser. "Hello, world!" should appear on the page. To use the API functionality, once the virtual environment is started, run 'python Hello.py' in a terminal window. In another terminal window run the command:
      curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Test","age":"100","occupation":"programmer"}' http://127.0.0.1/api/v1.0/addUsers
  
Note: Using the wrong quotation marks in the curl command will cause parse errors and will cause the program to fail. I have included a screenshot of my terminal windows when I successfully ran the program. 
