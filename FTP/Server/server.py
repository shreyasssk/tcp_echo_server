##########################################

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


authorizer = DummyAuthorizer()

########### USERS ####################
#first parameter is the username, second one is the password and the third one is the directory to which that particular user has access to

authorizer.add_user("Sahil", "Sahil", "/home/sahil/Documents", perm="elradfmwMT")
authorizer.add_user("Sharan", "Sharan", "/home/sahil/Documents", perm="elradfmwMT")
authorizer.add_user("Shreyask", "Shreyask", "/home/sahil/Documents", perm="elradfmwMT")
authorizer.add_user("Shreyass", "Shreyass", "/home/sahil/Documents", perm="elradfmwMT")
authorizer.add_user("Param", "Param", "/home/sahil/Documents", perm="elradfmwMT")
authorizer.add_user("Akash", "Akash", "/home/sahil/Documents", perm="elradfmwMT")
authorizer.add_user("Sumanth", "Sumanth", "/home/sahil/Documents", perm="elradfmwMT")

######################################

authorizer.add_anonymous("/home/sahil/Documents") #path of the directory you want to the clients to access
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("127.0.1.2", 8000), handler) #the IP address of your system, the one which is the server
server.serve_forever()
