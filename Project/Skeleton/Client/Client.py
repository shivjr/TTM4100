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
        ############## QT #################
        self.host = host
        self.server_port = server_port
        self.run()
        ###################################

    #Shiv
    def run(self):
        self.connection.connect((self.host, self.server_port))
        self.thread = ReceiveMessageWorker(client, self.connection)
        self.thread.deamon=True
        self.thread.run()

    #Shiv
    def disconnect(self):
        self.thread.stop = True
        self.connection.close()

    #Shiv     #LOOK INTO THIS
        #ARE WE SUPPOSED TO SOLVE HERE OR IN MESSAGEPARSER
    def receive_message(self, message):
        #Decode message
        msg_parser = MessageParser()
        decoded_message = msg_parser.parse(message)
        #Handle of the response, a.k.a decoded_message
        if(decoded_message['response'] == 'info'):
            print(msg_parser.parse_info(decoded_message))
        #elif(decoded_message['response'] == 'info'):
         #   print(' in Client.py: \t' + decoded_message['error'])
        pass

    #Shiv
    def send_payload(self, data):
        if(data.startswith('login')):
            try:
                username=data.split()[1]
            except IndexError:
                username=''
            payload = {'request': 'login', 'username': username}
        elif(data,startswith('logout')):
            payload = {'request': 'logout', 'None': None}
        elif(data,startswith('msg')):
            payload = {'request': 'msg', 'message': data.split(' ',1)[1]}
        elif(data,startswith('names')):
            payload = {'request': 'names', 'None': None}
        elif(data,startswith('help')):
            payload = {'request': 'help', 'None': None}
        else:
            print('send_payload() in Client.py: \t INVALID REQUEST')
        self.connection.sendall(json.dumps(data))



if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
    
    while True:
        input_= raw_input('>> ')
        client.send_payload(input_)

        if  input_== 'quit':
            break
    client.disconnect()
