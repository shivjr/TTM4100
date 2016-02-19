# -*- coding: utf-8 -*-
import socket
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser

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
        
        # TODO: Finish init process with necessary code
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        
    def disconnect(self):
        # TODO: Handle disconnection
        self.connection.close()
        ########
    def receive_message(self, message):
        # TODO: Handle incoming message
        recievedMessage = json.loads(message)
        if  recievedMessage.get('error') != None:
            print (recievedMessage.get('error'))
        elif recievedMessage.get('request') == 'login':
            print ('Welcome ' + recievedMessage.get('username') +'!')
        elif recievedMessage.get('request') == 'logout':
            print ('See you soon!')
        elif recievedMessage.get('request') == 'message':
            print('Your message is: ' + recievedMessage.get('message'))
        elif recievedMessage.get('request') == 'help':
            print('THIS NEEDS TO BE DONE. (func: recieve_message file: Client.py)')
        ###############################3

    def send_payload(self, data):
        # TODO: Handle sending of a payload
        
        pass
        
    # More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
