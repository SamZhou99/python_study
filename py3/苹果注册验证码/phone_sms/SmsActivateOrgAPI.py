import requests


class SmsActivateOrgAPI:
    def __init__(self) -> None:
        self.API_URL = "https://api.sms-activate.org/stubs/handler_api.php"
        self.API_KEY = "1212745A28e8f2772724bdfc334f16bf"

    # 查询余额
    def getBalance(self):
        rsp = self._getUrl({"action": "getBalance"})
        # ACCESS_BALANCE:412.78
        a = rsp.split(":")
        balance = a[1]
        return balance

    # 请求活动激活
    def getActiveActivations(self):
        return self._getUrl({"action": "getActiveActivations"})

    # 申请房间
    def getNumber(self, service="wx", country=12):
        return self._getUrl(
            {"action": "getNumberV2", "service": service, "country": country}
        )

    # 预租号码
    def getRentNumber(
        self, service="wx", country=12, webhook_url="http://149.28.74.54:8888/sms-hook"
    ):
        param = {"action": "getRentNumber", "service": service, "country ": country}
        if bool(webhook_url):
            param.update({"url": webhook_url})
        return self._getUrl(param)

    # 获取出租状态
    def getRentStatus(self, id):
        return self._getUrl({"action": "getRentStatus", "id": id})

    # 改变出租状态
    # status
    # 1 Finish
    # 2 Cancel
    def setRentStatus(self, id, status):
        return self._getUrl({"action": "setRentStatus", "id": id, "status": status})

    # 当前租号列表
    def getRentList(self):
        return self._getUrl({"action": "getRentList"})

    # 续租号码
    def getContinueRentNumber(self, id, rent_time):
        return self._getUrl(
            {"action": "continueRentNumber", "id": id, "rent_time": rent_time}
        )

    # 获取各国服务的价格
    def getPrices(self, service, country):
        return self._getUrl(
            {"action": "getPrices", "service": service, "country": country}
        )

    # 国家列表
    def getCountries(self):
        return self._getUrl({"action": "getCountries"})

    # API请求
    def _getUrl(self, parameter):
        param = {"api_key": self.API_KEY}
        param.update(parameter)
        rsp = requests.get(self.API_URL, param)
        if rsp.status_code != 200:
            return {"error": rsp.status_code}
        try:
            j = rsp.json()
        except:
            return rsp.text
        return j


# # 测试
# api = SmsActivateOrgAPI()

# # 租号码
# SmsRsp = Sms.getRentNumber("wx", 187)
# phone_number = SmsRsp["phone"]["number"]
# print(SmsRsp)
# {
#     "status": "success",
#     "phone": {
#         "id": 10527209,
#         "endDate": "2023-05-25 20:04:12",
#         "number": "79305055755",
#     },
# }
