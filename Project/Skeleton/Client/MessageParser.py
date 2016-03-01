import json

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            ######### Shiv #################
            'message': self.parse_message,
            'history': self.parse_history,
	    ################################	
        }

    def parse(self, json_object):
        ########### Shiv ###############
        payload = json.loads(json_object)
        ################################

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            # Response not valid
            return ('Her ender vi')
    ################### TODO ################
    def parse_error(self, payload):
        return ('Content: \t'+payload['content'])
    def parse_message(self, payload):
        return ('Content: \t'+payload['content'])
    def parse_history(self, payload):
        pass
    #########################################
    def parse_info(self, payload):
        message = ('Content: \t'+payload['content'])
        return message
  
