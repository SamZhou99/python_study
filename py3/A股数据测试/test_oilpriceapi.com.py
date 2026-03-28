import requests

url = "https://api.oilpriceapi.com/v1/prices/latest"
headers = {
    "Authorization": "Token eb0cd10ca525a81d26b14330ae1e6523",
    "Content-Type": "application/json",
}

response = requests.get(url=url, headers=headers)
data = response.json()
print(data)
