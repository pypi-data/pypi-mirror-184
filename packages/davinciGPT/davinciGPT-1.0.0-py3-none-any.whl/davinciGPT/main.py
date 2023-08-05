from requests import get


class Chatbot:
    def __init__(self, token):
        self.url = "https://codex-sfr4.onrender.com"
        self.token = token

    def chatbot(self, query):
        query = "+".join(query.split(" "))
        try:
            url = f"{self.url}/{query}"
            res = str(get(url).json()["bot"])
            result = " ".join(res.split())
            return result
        except:
            return "ERROR!! Chatbot not responding."
