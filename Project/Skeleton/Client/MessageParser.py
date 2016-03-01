

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

        #if payload['response'] in self.possible_responses:
        return self.possible_responses[payload['response']](payload)
        #else:
            # Response not valid
        pass
    ################### TODO ################
    def parse_error(self, payload):
        pass
    def parse_message(self, payload):
        pass
    def parse_history(self, payload):
        pass
    #########################################
    def parse_info(self, payload):
        message = 'Response: Info \t Content: '+ payload[info]
        return message
  
