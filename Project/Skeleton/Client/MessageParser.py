

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            # The keys below are added by Shiv
            'message': self.parse_message,
            'history': self.parse_history,
	    # More key:values pairs are maybe needed	
        }

    def parse(self, payload):
        payload = # decode the JSON object

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            # Response not valid

    def parse_error(self, payload):
    
    def parse_info(self, payload):
    
    # Include more methods for handling the different responses... 
