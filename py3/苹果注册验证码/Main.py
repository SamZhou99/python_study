import random
from collections.abc import Callable, Iterable, Mapping
from typing import Any
from BrowserDriver import BrowserDriver
from BrowserForm import BrowserForm
from english_name.FullEnglishName import FullEnglishName
from web_email_api.MailboxName import MailboxName
from phone_sms.SmsActivateOrgAPI import SmsActivateOrgAPI
from phone_sms.PhoneNumberFormat import PhoneNumberFormat
from ICloudLogin import iCoudLogin


def getFullName():
    FEName = FullEnglishName()
    name = FEName.FillName()
    first_name = name[0]
    last_name = name[1]
    return first_name, last_name


def getMailboxName():
    Mailbox = MailboxName()
    email = Mailbox.getName()
    # email = "alyssa@coinbtc.us"
    print("邮箱地址：{}".format(email))
    return email


def getShortName(country_code):
    f = open("./phone_sms/AppleCountry.txt", "r", encoding="utf-8")
    t = f.read()
    a = t.split("\n")
    country_code = str(country_code)
    for i in a:
        item = i.split(" ")
        print(item[3], country_code, item[3] == country_code)
        if item[3] == country_code:
            return item
    return None


def getCountryTag(country_id):
    f = open("./phone_sms/AppleCountry.txt", "r", encoding="utf-8")
    t = f.read()
    a = t.split("\n")
    country_id = str(country_id)
    for i in a:
        item = i.split(" ")
        if item[3] == country_id:
            # CN +86 中国大陆 3 China
            tag = item[0]
            area_code = item[1]
            cn = item[2]
            id = item[3]
            en = item[4]
            return tag, area_code, cn, id, en
    return None, None, None, None, None


def getPhoneNumber():
    ###############################################
    # 检查旧号码，用了几次。
    # 并且，看有同有超时。
    ###############################################
    test = False
    if test:
        phone_number = "639353094357"
        country_tag = "PH"
    else:
        # 3,中国,4,菲律宾
        country_id = 4
        country_tag, area_code, cn, id, en = getCountryTag(country_id)
        print(country_tag, area_code, cn, id, en)
        # 短信API
        Sms = SmsActivateOrgAPI()
        # 激活号码
        # SmsRsp = Sms.getNumber("wx", 187) #美国物理号
        SmsRsp = Sms.getNumber("wx", country_id)  # 菲律宾
        print("获取到激活号码：", SmsRsp)
        phone_number = SmsRsp["phoneNumber"]  # 639364544186
        phone_number = phone_number[len(area_code) - 1 :]
        print("可以输入的电话号码：", phone_number)
        # ################################
        # pformat = PhoneNumberFormat()
        # # 返回结果 ("+63", "9855654290")
        # country_number, phone_number = pformat.formatPhone(phone_number)
        # # 返回结果 ['PH', '+63', '菲律宾']
        # phone_prefix_tag = pformat.getPhoneNumberCountry(country_number)
        # # phone_number="9855654290",  country="PH"  # 菲律宾
    return {"phone_number": phone_number, "country": country_tag}


def getBirthday():
    y = random.randint(1970, 2004)
    m = random.randint(1, 12)
    d = random.randint(1, 30)
    if m == 2 and d > 28:
        d == random.randint(1, 28)
    if m < 10:
        m = "0" + str(m)
    if d < 10:
        d = "0" + str(d)
    birthday = "{}-{}-{}".format(y, m, d)
    return birthday


def getPassword():
    # password = "$aBc123XyZ#"
    paw = "!abcABC123@"
    return paw


def autoForm(driver):
    # 获取邮箱地址
    email = getMailboxName()
    print("邮箱地址：{}".format(email))

    phone_info = getPhoneNumber()
    phone_number = phone_info["phone_number"]
    country = phone_info["country"]
    print("电话号码：{}，国际区号简称：{}".format(phone_number, country))

    # 英文名全称
    first_name, last_name = getFullName()
    print("用户名：first_name:{}, last_name:{}".format(first_name, last_name))

    # 生日
    birthday = getBirthday()
    print("生日：{}".format(birthday))

    # 密码
    password = getPassword()
    print("密码：{}".format(password))

    # 填写表单
    form = BrowserForm(driver)
    # form.WindowSrcollBottom()
    form.SelectCountry()
    form.SelectCountryPhoneNumber(country)
    # 填写表单
    form.AutoInputForm(first_name, last_name, birthday, email, password, phone_number)
    return email, password, phone_number, country, first_name, last_name, birthday


def init():
    # 注册账号
    browser = BrowserDriver()
    driver = browser.Init(1024, 1024)
    browser.GoUrl()

    # 自动填写表单
    email, password, phone_number, country, first_name, last_name, birthday = autoForm(
        driver
    )
    print(
        "========== 用户完整信息 ==========",
        email,
        password,
        phone_number,
        country,
        first_name,
        last_name,
        birthday,
    )
    # 注册结束

    # 开始登录 www.icloud.com
    icoud = iCoudLogin(driver)
    icoud.Start(email, password, phone_number)

    browser.Close(60 * 10)


init()
