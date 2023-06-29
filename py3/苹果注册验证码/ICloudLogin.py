import requests, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class iCoudLogin:
    def __init__(self, driver: webdriver) -> None:
        self.URL = "https://www.icloud.com/"
        self.driver = driver

    def Start(self, account, password, phone_number):
        self.driver.get(self.URL)
        self.CssDisplayButton()
        self.ClickButtonLogin()
        self.IFrameFormLogin()
        self.InputAccountPassword(account, password)
        self.GetSmsCode(phone_number)
        self.SmsVerify(phone_number)
        self.SwitchToDefault()
        time.sleep(60 * 5)
        return True

    def CssDisplayButton(self):
        # 解决按钮隐藏状态的点击冲突
        self.driver.execute_script(
            """
btns=document.getElementsByTagName('button');
for(i=0;i<btns.length;i++){
    let b=btns[i]
    b.style.display='block';
    b.style.width=b.style.height='300px';
    b.innerText='BUTTON';
}
"""
        )
        return True

    def ClickButtonLogin(self):
        i = 0
        btns = self.driver.find_elements(By.TAG_NAME, "button")
        for item in btns:
            # 主要是点击 登录 按钮
            if i == 1:
                time.sleep(1)
                item.click()
                time.sleep(1)
            i += 1
        time.sleep(1)
        return True

    def IFrameFormLogin(self):
        time.sleep(1)
        # 等待出现登录表单
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        # 切换到iframe页操作
        iframe = self.driver.find_element(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(iframe)
        return True

    def InputAccountPassword(self, account, password):
        form_account = self.driver.find_element(By.ID, "account_name_text_field")
        form_account.send_keys(account)
        time.sleep(1)
        form_account.send_keys(Keys.ENTER)
        time.sleep(3)  # 提交等待
        form_password = self.driver.find_element(By.ID, "password_text_field")
        form_password.send_keys(password)
        time.sleep(1)
        form_password.send_keys(Keys.ENTER)
        time.sleep(3)  # 提交等待
        return True

    def GetSmsCode(self, phone_number):
        return phone_number

    def SmsVerify(self, phone_number):
        # 等待 短信验证输入界面
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "char5")))
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        code = ""
        print("请手动输入验证码。。。")
        time.sleep(60)
        # for item in inputs:
        #     time.sleep(1)
        #     type = item.get_attribute("type")
        #     id = item.get_attribute("id")
        #     if type == "tel" and len(code) >= i:
        #         item.send_keys(code[i])
        #         print(type, id, i, code[i])
        #         i += 1
        return True

    def SwitchToDefault(self):
        # 切换到默认页操作
        self.driver.switch_to.default_content()
        return True
