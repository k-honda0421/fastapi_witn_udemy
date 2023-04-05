import json

import requests


def main1():
    url = "http://0.0.0.0:8080/item/"
    body = {
        "name": "t-shirt",
        "description": "this is t-shirt",
        "price": 5980,
        "tax": 1.1
    }
    res = requests.post(url, json.dumps(body))
    print(res.json())


def main2():
    url = "http://0.0.0.0:8080/hello_data/"
    data = {
        "x": 1,
        "y": 3
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == "__main__":
    main1()
    main2()
