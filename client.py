import json

import requests


def get_cuisine(data):
    url = "http://localhost:5000/cuisine/"+data
    response = requests.post(url)
    response = json.load(response)
    return response


print(get_cuisine("indian"))
