import requests


class SmsManAPI:
    def __init__(self) -> None:
        self.TO_KEN = "XWRhJ2A_r_6Y-EogMGziNCg-ZHbqINry"

    def _get(self, act, parameter=None):
        url = "http://api.sms-man.com/control/{}".format(act)
        params = {"token": self.TO_KEN}
        if parameter:
            params.update(parameter)
        rsp = requests.get(url, params)
        return rsp.json()

    # 余额
    def Balance(self):
        return self._get("get-balance")

    # 获取号码
    def GetNumber(self, country_id, application_id):
        return self._get(
            "get-number", {"country_id": country_id, "application_id": application_id}
        )

    # 短信内容
    def GetSms(self, request_id):
        return self._get("get-sms", {"request_id": request_id})

    # 修改状态
    def SetStatus(self, request_id, status):
        return self._get("set-status", {"request_id": request_id, "status": status})

    # 国家列表
    def GetCountries(self):
        return self._get("countries")

    # 服务列表
    def GetApplications(self):
        return self._get("applications")


# api = SmsManAPI()
# rsp = api.Balance()
# print(rsp["balance"])

# rsp = api.GetCountries()
# for i in rsp:
#     print(rsp[i]["id"], rsp[i]["code"], rsp[i]["title"])

# rsp = api.GetApplications()
# for i in rsp:
#     if rsp[i]["title"].find("Apple") > 0:
#         print(rsp[i])
# # import json
# # txt = json.dumps(rsp)
# # f = open("./app.txt", "a")
# # f.write(txt)
# # f.close()

# rsp = api.GetNumber(8, 297)
# print(rsp)
# {
#     "request_id": 221651596,
#     "application_id": 297,
#     "country_id": 8,
#     "number": "639295835583",
# }

# rsp = api.GetSms("221651596")
# print(rsp)


class SmsManRentAPI:
    def __init__(self) -> None:
        self.TO_KEN = "XWRhJ2A_r_6Y-EogMGziNCg-ZHbqINry"

    def _get(self, act, parameter=None):
        url = "http://api.sms-man.com/rent-api/{}".format(act)
        params = {"token": self.TO_KEN}
        if parameter:
            params.update(parameter)
        rsp = requests.get(url, params)
        return rsp.json()

    def Balance(self):
        return self._get("get-balance")

    def Limit(self, country_id=1, type="hour", time=4):
        return self._get(
            "limits", {"country_id": country_id, "type": type, "time": time}
        )

    def GetNumber(self, country_id=1, type="hour", time=4):
        return self._get(
            "get-number", {"country_id": country_id, "type": type, "time": time}
        )

    def SetStatus(self, request_id, status):
        return self._get("set-status", {"request_id": request_id, "status": status})

    def GetSms(self, request_id):
        return self._get("get-sms", {"request_id": request_id})

    def GetAllSms(self, request_id):
        return self._get("get-all-sms", {"request_id": request_id})


# api = SmsManRentAPI()

# rsp = api.Balance()
# print(rsp)

# rsp = api.Limit(1)
# print(rsp)

# rsp = api.GetNumber()
# print(rsp)
# {'request_id': 44274, 'application_id': 0, 'country_id': 1, 'number': '79210093229'}

# rsp = api.GetSms("44274")
# print(rsp)
# {
#     "request_id": 44274,
#     "application_id": 0,
#     "country_id": 1,
#     "number": "79210093229",
#     "sms": {
#         "text": "Apple ID 代码为：974210。请勿与他人共享。 ",
#         "code": "974210",
#         "time": "2023-05-28 11:09:45",
#     },
# }

# rsp = api.GetAllSms("44274")
# print(rsp)
# {
#     "request_id": 44274,
#     "application_id": 0,
#     "country_id": 1,
#     "number": "79210093229",
#     "sms": [
#         {
#             "text": "Apple ID 代码为：330428。请勿与他人共享。 @icloud.com #330428 %apple.com ",
#             "code": "330428",
#             "time": "2023-05-28 11:12:13",
#         },
#         {
#             "text": "Apple ID 代码为：974210。请勿与他人共享。 ",
#             "code": "974210",
#             "time": "2023-05-28 11:09:45",
#         },
#     ],
# }
