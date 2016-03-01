# -*- coding: utf-8 -*-
from threading import Thread

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and it allows
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """
        # Flag to run thread as a deamon
        ########## Shiv ###########
        self.daemon = True
        self.client = client
        self.connection = connection
        self.stop = False
        ###########################
    def run(self):
        ########## Shiv ###########
        while not self.stop:
            data = self.connection.recv(2480) # Unsure about how large the number should be
            self.client.receive_message(data)
        ###########################

