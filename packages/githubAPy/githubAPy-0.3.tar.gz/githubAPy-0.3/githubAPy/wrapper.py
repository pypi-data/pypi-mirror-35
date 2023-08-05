import requests
import json
import base64


class gapy:

    error_message = """Error occured while processing the request.
                        Please check the access token and try again."""

    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            "Accept":"application/vnd.github.machine-man-preview+json",
            "Authorization":"bearer "+self.access_token,
            "Content-Type":"application/json",
        }
        self.url = "https://api.github.com/"

    def me(self):
        """ Returns the user's info """
        endpoint = self.url+'user'
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(self.error_message)

    def user(self, username):
        """ Return info of a GitHub user """
        endpoint = self.url+'users/{}'.format(username)
        response = request.get(endpoint, headers=self.headers)
        if response.status_code == 200:
            return json.load(response.text)
        else:
            raise Exception(self.error_message)
