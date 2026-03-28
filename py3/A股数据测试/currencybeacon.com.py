# https://currencybeacon.com/account/dashboard
# https://api.currencybeacon.com/v1/latest?api_key=73dGLQJzJoQ5PlaZdF3gpXH9O0n6G8ZQ#
# https://pypi.org/project/akshare/

# import requests

# TOKEN = "73dGLQJzJoQ5PlaZdF3gpXH9O0n6G8ZQ"
# REQ_URL = "https://api.currencybeacon.com/v1/latest"

# params = {
#     "api_key": TOKEN,
# }
# response = requests.get(REQ_URL, params=params)
# print(response.json())

f = open("currencybeacon.com_latest.json", "r", encoding="utf-8")
latest_json = f.read()
f.close()
print(latest_json)
