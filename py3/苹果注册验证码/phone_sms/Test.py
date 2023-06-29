from SmsActivateOrgAPI import SmsActivateOrgAPI

sms = SmsActivateOrgAPI()

# rsp = sms.getBalance()
# print(rsp)

# rsp = sms.getActiveActivations()
# print(rsp)

# rsp = sms.getCountries()
# print(rsp)

# rsp = sms.getPrices("wx", 12)
# print(rsp)

# rsp = sms.getRentList()
# print(rsp)

rsp = sms.getNumber()
print(rsp)
{
    "activationId": "1483637249",
    "phoneNumber": "19145355732",
    "activationCost": "10.00",
    "countryCode": "12",
    "canGetAnotherSms": True,
    "activationTime": "2023-05-24 12:20:25",
    "activationOperator": "any",
}

rsp = sms.getRentList()
print(rsp)
