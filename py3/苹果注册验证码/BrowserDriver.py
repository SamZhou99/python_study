import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


class BrowserDriver:
    def __init__(self) -> None:
        self.REG_URL = "https://appleid.apple.com/account"
        self.CHROME_DRIVER = "./chromedriver/chromedriver_win32.exe"
        self.PROXY_IP_ARR = ["--proxy-server=http://171.35.141.103:9999"]
        # self.PROXYIP = random.choice(self.PROXY_IP_ARR)
        self.PROXYIP = self.PROXY_IP_ARR[0]
        self.chrome_options = None
        self.driver = None

    def Init(self, w=1024, h=768):
        if self.chrome_options:
            self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        else:
            self.driver = webdriver.Chrome()

        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(w, h)
        return self.driver

    def Proxy(self):
        # 代理设置
        self.chrome_options = Options()
        self.chrome_options.add_argument(self.PROXYIP)
        return True

    def GoUrl(self):
        self.driver.get(self.REG_URL)
        assert "Apple" in self.driver.title
        time.sleep(3)
        return True

    def Close(self, ts=1):
        time.sleep(ts)
        self.driver.close()
