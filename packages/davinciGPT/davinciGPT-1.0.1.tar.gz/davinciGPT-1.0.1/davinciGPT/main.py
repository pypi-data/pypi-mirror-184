from requests import post
import json


class Chatbot:
    def __init__(self, token):
        self.url = "https://codex-sfr4.onrender.com/"
        self.token = token

    def chatbot(self, query):
        try:
            body = {"prompt": query}
            res = post(self.url, json=body)
            res = str(res.json()["bot"])
            result = " ".join(res.split())

            return result
        except:
            return "ERROR!! Chatbot not responding."
