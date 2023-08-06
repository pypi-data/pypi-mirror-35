import requests

class Client(object):
    base_url = 'https://devdrip.herokuapp.com'
    api_token = ''

    def __init__(self, api_token):
        self.api_token = api_token

    # to_phone_number does not need country code
    def create_message(self, to_phone_number, message_text):
        r = requests.post(
            self.base_url+'/message',
            data={
                'api_token': self.api_token,
                'phone_number': to_phone_number,
                'message': message_text
            }
        )

        if r.status_code == requests.codes.ok:
            return True, ''
        return False, 'Server error. Please try again'
