import json

import requests


def get_cuisine(data):
    url = "http://localhost:5000/cuisine/"+data
    response = requests.get(url)
    response.status_code == 200
    return response


print(get_cuisine("german"))
