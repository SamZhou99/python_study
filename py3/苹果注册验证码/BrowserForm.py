import time, base64, requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BrowserFormImgCode import BrowserFormImgCode
from EMailCode import EMailCode

from phone_sms.SmsManAPI import SmsManRentAPI
from phone_sms.SmsActivateOrgAPI import SmsActivateOrgAPI


class BrowserForm:
    def __init__(self, driver) -> None:
        self.driver = driver
        # self.captcha_input = None

    # 窗口滚动到底部
    def WindowSrcollBottom(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        return True

    # 选择国家
    def SelectCountry(self, country="USA"):
        time.sleep(1)
        select = Select(self.driver.find_element(By.TAG_NAME, "select"))
        select.select_by_value(country)  # select.select_by_visible_text("美国")
        return True

    # 选择国家电话号码区位
    def SelectCountryPhoneNumber(self, country="US"):
        time.sleep(3)
        labels = self.driver.find_elements(By.CLASS_NAME, "visuallyhidden")
        for label in labels:
            select_id = label.get_attribute("for")
            print(select_id)
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located((By.ID, select_id)))
        select = Select(self.driver.find_element(By.ID, select_id))
        select.select_by_value(country)
        # opts = select.options
        # for item in opts:
        #     print(item.text, item.get_attribute("value"))
        return True

    # 自动填写表单
    def AutoInputForm(self, first_name, last_name, birthday, mail, password, phone):
        time.sleep(5)
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        i = 0
        for input in inputs:
            # logInputInfo(input, i)
            if i in [3, 4, 5, 6, 7, 8, 9, 14]:
                time.sleep(2)
            if i == 3:
                # 姓氏
                input.send_keys(last_name)
                input.send_keys(Keys.RETURN)
            if i == 4:
                # 名称
                input.send_keys(first_name)
                input.send_keys(Keys.RETURN)
            if i == 5:
                # 生日
                input.send_keys(birthday)
                input.send_keys(Keys.RETURN)
            if i == 6:
                # 邮箱地址
                input.send_keys(mail)
                input.send_keys(Keys.RETURN)
            if i == 7 or i == 8:
                # 密码
                input.send_keys(password)
                input.send_keys(Keys.RETURN)
            if i == 9:
                # 电话
                input.send_keys(phone)
                input.send_keys(Keys.RETURN)
            if i == 14:
                # 验证码
                # self.captcha_input = input
                img_path = saveImg(self.driver)
                code = getCaptcha(img_path)
                input.send_keys(code)
                # 看看验证对不对
                time.sleep(10)
                # 提交表单
                input.send_keys(Keys.RETURN)
                # 提交后，打开了新的页面，等待邮件验证码？
                time.sleep(10)
                # 获取验证码INPUT
                # 去获取邮件中的验证码
                # 输入邮件验证码
                InputCaptcha(self.driver, mail)
                # 获取手机验证码
                time.sleep(10)
                ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                setPhoneInputCode(self.driver, phone, ts)
            i += 1
        return True


# 输入验证码
def InputCaptcha(driver, mail):
    time.sleep(1)
    code = ""
    # 每N秒请求一次邮件验证码，是否收到，循环100次。
    for i in range(100):
        code = getEmailCaptcha(mail)
        if code:
            break
        time.sleep(6)
    print("从邮箱中获取到验证码：{}".format(code))

    # 等待输入验证码的表单
    wait = WebDriverWait(driver, 60)
    inputFromChar = wait.until(EC.presence_of_element_located((By.ID, "char0")))
    print(
        "邮箱验证码，等待条件成立",
        inputFromChar.get_attribute("type"),
        inputFromChar.get_attribute("id"),
    )

    time.sleep(1)
    i = 0
    for c in code:
        inputs = driver.find_elements(By.ID, "char{}".format(i))
        for input in inputs:
            input.send_keys(c)
            time.sleep(0.3)
        i += 1
    input.send_keys(Keys.RETURN)
    time.sleep(1)
    return True


# 从邮件中获取验证码
def getEmailCaptcha(mail):
    url = "http://149.28.74.54:8888/email/{}".format(mail)
    rsp = requests.get(url)
    if rsp.status_code != 200:
        return False

    j = rsp.json()
    if j["data"]:
        try:
            return j["data"]["captcha"]
        except:
            print("error")
    return False


# 输入手机验证码
def setPhoneInputCode(driver, phone, ts):
    print("等待手机接受验证码。。。{}".format(phone))
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    inputFromChar = wait.until(EC.presence_of_element_located((By.ID, "char0")))
    print(
        "{}, 手机验证码，等待条件成立".format(phone),
        inputFromChar.get_attribute("type"),
        inputFromChar.get_attribute("id"),
    )

    print("获取手机验证码，并，输入手机验证码页。{}".format(phone))
    time.sleep(1)

    for i in range(100):
        time.sleep(2)
        url = "http://127.0.0.1:6789/sms/{}/{}".format(phone, ts)
        print(url)
        rsp = requests.get(url)
        if rsp.status_code != 200:
            continue

        try:
            json_result = rsp.json()
            if len(json_result["data"]) <= 0:
                # 验证码数据没有，继续请求
                continue
            break
        except:
            print("======================================")
            print("解析短信json格式可能错误。请求次数:{}", i)
            print(rsp.text)
            print("======================================")

    code = json_result["data"][0]["code"]
    print("code:{}".format(code))

    i = 0
    for c in code:
        input = driver.find_element(By.ID, "char{}".format(i))
        i += 1
        input.send_keys(c)
        time.sleep(0.5)
    input.send_keys(Keys.RETURN)
    time.sleep(60)
    return True


# 获取验证码
def getCaptcha(img_path):
    time.sleep(1)
    imgCode = BrowserFormImgCode()
    print("1账户余额:", imgCode.QueryBalc())
    rsp = imgCode.Verify(img_path)
    code = "-"
    # rsp.ret_code：正常返回0
    # rsp.request_id：唯一订单号
    # rsp.pred_rsp.value：识别结果
    # rsp.err_msg：异常时返回异常详情
    if rsp.ret_code == 0:
        code = rsp.pred_rsp.value
    else:
        print(rsp.err_msg)
        print("打码错误，手动操作吧。")
        return False
    print("2账户余额:", imgCode.QueryBalc())
    print("打码返回的结果：", rsp.ret_code, rsp.request_id, rsp.pred_rsp.value, rsp.err_msg)
    time.sleep(1)
    return code


# 保存图片
def saveImg(driver):
    # 获得验证码图片，方法二 # 获取验证码src的base64编码，解码并保存为图片。
    time.sleep(1)
    ts = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    img_path = "./code_img/{}.jpg".format(ts)
    imgs = driver.find_elements(By.TAG_NAME, "img")
    for img in imgs:
        # print(img.get_attribute("src"), img.get_attribute("alt"))
        if img.get_attribute("alt") == "安全提示图片":
            for i in range(20):
                img_base64 = img.get_attribute("src")
                if len(img_base64) > 100:
                    img_base64 = img_base64.split(" ")[1]
                    data = base64.b64decode(img_base64)
                    with open(img_path, "wb") as f:
                        f.write(data)
                    break
                if i >= 19:
                    return ""
                time.sleep(2)
        print("验证码保存完成", img_path)
    time.sleep(1)
    return img_path


# 打印日志
def logInputInfo(input, i):
    try:
        print(
            "{} 表单类型：{},表单ID：{}".format(
                i, input.get_attribute("type"), input.get_attribute("id")
            )
        )
        return True
    except:
        return False


# import requests

# rsp = requests.get(
#     "http://127.0.0.1:6789/sms/{}/{}".format("15346665627", "2023-5-31 22:59:8")
# )
# if rsp.status_code == 200:
#     print(rsp.json())
