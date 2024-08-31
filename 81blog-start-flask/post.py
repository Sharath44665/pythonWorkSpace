
import requests
class Post:
    def __init__(self):
        response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()

        self.fakeData = response.json()

    def getData(self):
        return self.fakeData
