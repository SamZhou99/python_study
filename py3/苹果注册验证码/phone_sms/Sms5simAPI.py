import requests


class Sms5simAPI:
    def __init__(self) -> None:
        self.DOMAIN = "5sim.net"
        # self.API_URL = "https://{}/v1/user/profile".format(self.DOMAIN)
        self.API_KEY = "1212745A28e8f2772724bdfc334f16bf"
        self.TO_KEN = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY3MTIzMzUsImlhdCI6MTY4NTE3NjMzNSwicmF5IjoiNjEzYzgzYzY4ZGI2NmRjZGU2YzdmYTgyZjY5ZmIyOGEiLCJzdWIiOjE2NjMwNDd9.2ijNSWawkEuzoF3U2KTqn1-UwkwrTT9Mtw4uMkLE154uWxNDzXdonWfKhzYqH0HTJx8mM3Ew38UKIw9MfV9vrwmUZCujYREM-HghC7R7yx8H_o1mUsPh0VkcTZTChHJpPR_gNkZZMr4v2k9BV7gYQGIl_iKOWSrZvYkolpSgMxAtaKYmYgoBTG5nqC0oYv_X6YY8bfh126CXo3GZDOYhtosjYCWAF7HiUtdyD2HziyoDhfrsjtEMBV8freDl5rLYrE6abo9q5T6ROTmfGX6wkrdbeuZaOUfeUg12TZiq7A1pB6OILY7GxNbtKH-hcA7HP66lnuYB9Hr9AChcn-6_Lw"

    def _get(self, act):
        headers = {
            "Authorization": "Bearer " + self.TO_KEN,
            "Accept": "application/json",
        }
        URL = "https://{}/v1/{}".format(self.DOMAIN, act)
        rsp = requests.get(URL, headers=headers)
        if rsp.status_code != 200:
            return rsp
        try:
            return rsp.json()
        except:
            pass
        try:
            return rsp.text
        except:
            pass
        return rsp

    def Balance(self):
        rsp = self._get("user/profile")
        return rsp

    def BuyActivationNumber(
        self, country="philippines", product="apple", operator="any"
    ):
        # operator = "globe"  # "any"
        rsp = self._get(
            "user/buy/activation/{}/{}/{}".format(country, operator, product)
        )
        return rsp

    def GetNotifications(self):
        rsp = self._get("guest/flash/en")
        return rsp


# api = Sms5simAPI()
# rsp = api.Balance()
# print(rsp["balance"])

# rsp = api.BuyActivationNumber("philippines", "apple", "globe")
# print(rsp)
# {
#     "id": 460503213,
#     "phone": "+639090596140",
#     "operator": "virtual32",
#     "product": "apple",
#     "price": 28,
#     "status": "RECEIVED",
#     "expires": "2023-05-27T09:14:02.850588875Z",
#     "sms": None,
#     "created_at": "2023-05-27T09:04:02.850588875Z",
#     "country": "philippines",
# }

# rsp = api.GetNotifications()
# print(rsp)
