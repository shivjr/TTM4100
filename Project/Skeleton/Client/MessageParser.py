import json

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history,	
        }

    def parse(self, json_object):
        payload = json.loads(json_object)
        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            # Response not valid
            pass
    def parse_error(self, payload):
        return (payload['content'])
    def parse_message(self, payload):
        return (payload['content'])
    def parse_history(self, payload):
        return (payload['content'])
    def parse_info(self, payload):
        message = (payload['content'])
        return message
  
