import requests, time, io, base64, random, string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains  # AchtionChains

# from selenium.webdriver.support.ui import Ui
# import org.openqa.selenium.support.ui.Select

from PIL import Image


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# chrome和driver版本一定要一致，否则可能报错
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

REG_URL = "https://appleid.apple.com/account"
CHROME_DRIVER = "./chromedriver/chromedriver_win32.exe"
DRIVER_OPTIONS = webdriver.ChromeOptions()

# 代理设置
chrome_options = Options()
chrome_options.add_argument("--headless")  # 隐身模式

# # 手机模式
# mobile_emulation = {"deviceName": "iPhone X"}
# options = Options()
# options.add_experimental_option("mobileEmulation", mobile_emulation)

# PROXY_IP_ARR = ["--proxy-server=http://171.35.141.103:9999"]
# PROXYIP = random.choice(PROXY_IP_ARR)
# chrome_options.add_argument(PROXYIP)
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()
driver.set_window_position(0, 0)
driver.set_window_size(1200, 1200)
# driver.get(REG_URL)
# # print(driver.page_source())
# assert "Apple" in driver.title
# elem = driver.find_element(By.NAME, "wd")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


# div = driver.find_element(By.CLASS_NAME, "img-wrapper")
# img = div.find_element(By.TAG_NAME, "img")
# print(img)


# img_x, img_y = img.location.values()
# # img_w, img_h = img.size.values()
# img_w, img_h = 120, 58
# img_data = driver.get_screenshot_as_png()
# # print(img_data)

# # 滚动到页面底部
# time.sleep(1)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 获得验证码图片，方法一 # 截图保存，验证码。前提需要窗口大小固定，这个坐标才会固定。
# time.sleep(1)
# img_m = 1
# img_x, img_y = 458, 132
# img_w, img_h = 180 * img_m, 90 * img_m
# img_data = driver.get_screenshot_as_png()
# img_bytes = Image.open(io.BytesIO(img_data))
# img_code = img_bytes.crop((img_x, img_y, img_x + img_w, img_y + img_h))
# img_code.save("./code_img/test.png")
# # img_code.show()

# 获得验证码图片，方法二 # 获取验证码src的base64编码，解码并保存为图片。
# time.sleep(1)
# imgs = driver.find_elements(By.TAG_NAME, "img")
# for img in imgs:
#     # print(img.get_attribute("src"), img.get_attribute("alt"))
#     if img.get_attribute("alt") == "安全提示图片":
#         img_base64 = img.get_attribute("src")
#         img_base64 = img_base64.split(" ")[1]
#         data = base64.b64decode(img_base64)
#         with open("./code_img/test.jpg", "wb") as f:
#             f.write(data)
#     print("验证码保存完成")

# driver.save_screenshot("./code_img/test.png")


# # 选择国家
# time.sleep(1)
# select = Select(driver.find_element(By.TAG_NAME, "select"))
# select.select_by_value("USA")
# # select.select_by_visible_text("美国")

# time.sleep(5)
# labels = driver.find_elements(By.CLASS_NAME, "visuallyhidden")
# for label in labels:
#     select_id = label.get_attribute("for")
#     print(select_id)
# wait = WebDriverWait(driver, 3)
# inputFromChar = wait.until(EC.presence_of_element_located((By.ID, select_id)))
# select_area = Select(driver.find_element(By.ID, select_id))
# # select_area.select_by_value("US")

# print("快显示OPTIONS")
# opt = select_area.options
# # for i in opt:
# #     print(i.text, i.get_attribute("value"))
# print("3 select", len(opt))
# # time.sleep(5)

# # 表单
# time.sleep(3)
# inputs = driver.find_elements(By.TAG_NAME, "input")
# i = 0

# pw = "".join(random.sample(string.ascii_lowercase + string.digits, 3))
# pw = pw + "".join(random.sample(string.ascii_uppercase + string.digits, 3))
# pw = pw + "".join(random.sample(string.hexdigits + string.digits, 3))
# print("密码：" + pw)

# for input in inputs:
#     print(
#         "{} 表单类型：{},表单ID：{}".format(
#             i, input.get_attribute("type"), input.get_attribute("id")
#         )
#     )
#     # input.send_keys("1")
#     # input.send_keys(Keys.RETURN)
#     i += 1

time.sleep(1)
driver.get("https://www.icloud.com/")
wait = WebDriverWait(driver, 2)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
# wait.until(EC.visibility_of_any_elements_located((By.TAG_NAME, "button")))
time.sleep(2)
# buttons_ui = driver.find_elements(By.TAG_NAME, "ui-button")
# i = 0
# for btn_ui in buttons_ui:
#     type = btn_ui.get_attribute("type")
#     id = btn_ui.get_attribute("id")
#     label = btn_ui.text
#     print(type, id, label)
#     if label == "登录":
#         time.sleep(1)
#         # btn.click()
#         # btn.send_keys("\t")
#         # btn.send_keys(Keys.RETURN)
#         j = 0
#         buttons = driver.find_elements(By.TAG_NAME, "button")
#         for btn in buttons:
#             ActionChains(driver).move_to_element(btn_ui).click(btn_ui).perform()
#             time.sleep(1)
#             j += 1

#     # if i == 1:
#     #     btn.click()
#     i += 1

driver.execute_script(
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
i = 0
btns = driver.find_elements(By.TAG_NAME, "button")
for item in btns:
    if i == 1:
        time.sleep(2)
        print(i)
        # ActionChains(driver).move_to_element(item).click(item).perform()
        item.click()
        time.sleep(2)
    i += 1

time.sleep(2)

wait = WebDriverWait(driver, 8)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))

# 切换到iframe页操作
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
# 切换到默认页操作
# driver.switch_to.default_content()

# print("find inputs")
# inputs = driver.find_elements(By.TAG_NAME, "input")
# print(inputs)
# for i in inputs:
#     type = i.get_attribute("type")
#     id = i.get_attribute("id")
#     print(type, id)

account = driver.find_element(By.ID, "account_name_text_field")
ActionChains(driver).move_to_element(account).click(account).perform()
account.send_keys("amber@coinbtc.us")
time.sleep(1)
account.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element(By.ID, "password_text_field")
password.send_keys("!abcABC123@")
time.sleep(1)
password.send_keys(Keys.ENTER)
time.sleep(7)

# 等待短信验证
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "char5")))
inputs = driver.find_elements(By.TAG_NAME, "input")
code = "1234567890"
for item in inputs:
    time.sleep(1)
    type = item.get_attribute("type")
    id = item.get_attribute("id")
    if type == "tel":
        item.send_keys(code[i])
        print(type, id, i, code[i])
        i += 1


time.sleep(60 * 10)
driver.close()
