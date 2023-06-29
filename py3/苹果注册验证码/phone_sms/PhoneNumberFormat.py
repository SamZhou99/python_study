class PhoneNumberFormat:
    def __init__(self) -> None:
        pass

    # 电话号码格式化
    def formatPhone(self, phone):
        if not phone:
            return None
        index = phone.find(" ")
        country_number = ""
        phone_number = ""
        if index != -1:
            country_number = phone[:index]
            country_number = country_number.strip()
            phone_number = phone[index:]
            phone_number = phone_number.replace(" ", "")
            phone_number = phone_number.replace("(", "")
            phone_number = phone_number.replace(")", "")
            phone_number = phone_number.strip()
        # country = "RU"  # 俄罗斯
        # country = "PH"  # 菲律宾
        # country = "CN"  # 中国
        return country_number, phone_number

    # 通过国际区号，获取相关信息
    def getPhoneNumberCountry(self, country_number):
        f = open("./phone_sms/ApplePhoneShortName.txt", "r", encoding="utf-8")
        t = f.read()
        countrys = t.split("\n")
        for line_txt in countrys:
            item = line_txt.split(" ")
            if item[1] == country_number:
                # (CN, +86, 中国大陆)
                return item
        return None


# # phone_number = "+86 15346665627"
# phone_number = "+63 (929) 717 98 55"

# api = PhoneNumberFormat()

# rsp = api.formatPhone(phone_number)
# print(rsp)

# short_name = api.getPhoneNumberCountry(rsp[0])
# print(short_name)
