# -*- coding: utf-8 -*-
import SocketServer
import re #regex class, used to check if username is valid
import time
import datetime
"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

"""
regex for å sjekke om det er A-z,a-z,0-9:
^[A-Za-z0-9_.]+$
"""

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """
    #Shiv
    def pretty_print(self, message, username, timestamp):
        return username + ' said @ ' + timestamp + ": " + message
    #Shiv
    def printConnection(self, port, ip):
        print ('Client connected @' + ip +':'m + str(port))
    #Shiv
    def handle_login(self, message):
        username = message['username'];
        if not re.match('w+\^$', username):
            data = {'response': 'error', 'content': 'Invalid username', 'username':username}
        elif username in self.server.clientsvalues():
            data = {'response': 'error', 'content': 'Username taken', 'username':username}
        else:
            self.server.clients[self.connection] = username
            data = {'response': 'info', 'content': 'Login successful', 'username':username}
        self.connection.sendall(json.dumps(data))
    #Shiv
    def handle_logout(self):
        if self.connection in self.server.clients:
            username = self.server.clients[self.connection]
            data = {'response': 'info', 'content': 'Logout successful', 'username':username}
            del self.server.clients[self.connection]
        else:
            data = {'response': 'error', 'content': 'Not logged in'}
        self.connection.sendall(json.dumps(data))
    #Shiv
    def handle_msg(self, message):
        if self.connection in self.server.clients:
            username = self.server.clients[self.connection]
            st = datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y %H:%M:%S')
            msg = self.pretty_print(message['msg'], username, st)
            self.server.messages.append(msg)
            data = {'response': 'message', 'content': msg}
        else:
            data = {'response': 'error', 'content': 'Not logged in'}
        self.connection.sendall(json.dumps(data))
    def handle_names:
        pass
    def handle_help:
        pass
    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        ############## Shiv ##############################
        self.printConnection(self.port, self.ip)
        # Loop that listens for messages from the client
        while True:
            data = self.connection.recv(2048).strip()
            if data:
                message = json.loads(data)
                request = message.get('request')
                if(request == 'login'):
                    self.handle_login(message)
                elif(request == 'logout'):
                    self.handle_logout(message)
                elif(request == 'msg'):
                    self.handle_msg(message)
                elif(request == 'names'):
                    self.handle_names(message)
                elif(request == 'help'):
                    self.handle_help(message)
                #else:
                 #   break
        #####################################################
        
    
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True
    ######### Shiv ###########
    messages = []
    clients = []
    ##########################
if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
