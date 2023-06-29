import requests


def getAddress():
    url = "https://www.meiguodizhi.com/api/v1/dz"
    myobj = {"city": "", "method": "refresh", "path": "/usa-address/oregon"}
    x = requests.post(url, json=myobj)
    print(x.text)


def getJSON():
    resp = requests.get("https://api.coinbtc.us/api/test/ip")
    print(resp.json())


def init():
    # getAddress()
    getJSON()


init()
