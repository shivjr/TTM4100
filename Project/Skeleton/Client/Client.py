# -*- coding: utf-8 -*-
import socket
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser
import json
class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object 
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ############## QT #################
        self.host = host
        self.server_port = server_port
        self.run()
        ###################################

    #Shiv
    def run(self):
        self.connection.connect((self.host, self.server_port))
        self.thread = MessageReceiver(self, self.connection)
        self.thread.deamon=True
        self.thread.start()
        while True:
            input_= raw_input('>> ')
            self.send_payload(input_)

            if  input_== 'quit':
                break
        self.disconnect()
        

    #Shiv
    def disconnect(self):
        self.thread.stop = True
        self.connection.close()

    #Shiv 
    def receive_message(self, message):
        #Decode message
        msg_parser = MessageParser()
        print(message)
        if message is None:
            print('oops its none')
        decoded_message = msg_parser.parse(message)
        #Print the "handled" response
        print(decoded_message)
    #Shiv
    def send_payload(self, data):
        if(data.startswith('login')):
            try:
                username=data.split()[1]
            except IndexError:
                username=''
            payload = {'request': 'login', 'username': username}
        elif(data.startswith('logout')):
            payload = {'request': 'logout', 'None': None}
        elif(data.startswith('msg')):
            payload = {'request': 'msg', 'content': data.split(' ',1)[1]}
        elif(data.startswith('names')):
            payload = {'request': 'names', 'None': None}
        elif(data.startswith('help')):
            payload = {'request': 'help', 'None': None}
        else:
            payload = {'request': '', 'None': None}
        self.connection.sendall(json.dumps(payload))



if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9996)
    

