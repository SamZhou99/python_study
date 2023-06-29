import requests, time, io, base64, random, string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

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
# PROXY_IP_ARR = ["--proxy-server=http://171.35.141.103:9999"]
# PROXYIP = random.choice(PROXY_IP_ARR)
# chrome_options.add_argument(PROXYIP)
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()
driver.set_window_position(1024, 0)
driver.set_window_size(1024, 1024)
driver.get(REG_URL)
# print(driver.page_source())
assert "Apple" in driver.title
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


# 选择国家
time.sleep(1)
select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_value("USA")
# select.select_by_visible_text("美国")

time.sleep(5)
print("1 select")
labels = driver.find_elements(By.CLASS_NAME, "visuallyhidden")
for label in labels:
    select_id = label.get_attribute("for")
    print(select_id)
wait = WebDriverWait(driver, 5)
inputFromChar = wait.until(EC.presence_of_element_located((By.ID, select_id)))
print("2 select")
select_area = Select(driver.find_element(By.ID, select_id))
# select_area.select_by_value("US")

print("快显示OPTIONS")
opt = select_area.options
for i in opt:
    print(i.text, i.get_attribute("value"))
print("3 select")
time.sleep(10)

# 表单
time.sleep(5)
inputs = driver.find_elements(By.TAG_NAME, "input")
i = 0

pw = "".join(random.sample(string.ascii_lowercase + string.digits, 3))
pw = pw + "".join(random.sample(string.ascii_uppercase + string.digits, 3))
pw = pw + "".join(random.sample(string.hexdigits + string.digits, 3))
print("密码：" + pw)

for input in inputs:
    print(
        "{} 表单类型：{},表单ID：{}".format(
            i, input.get_attribute("type"), input.get_attribute("id")
        )
    )
    time.sleep(0.5)
    if i == 3:
        # 姓氏
        input.send_keys("peter")
        input.send_keys(Keys.RETURN)
    if i == 4:
        # 名称
        input.send_keys("huang")
        input.send_keys(Keys.RETURN)
    if i == 5:
        # 生日
        input.send_keys("20000625")
        input.send_keys(Keys.RETURN)
    if i == 6:
        # 邮箱地址
        random_str = "".join(random.sample(string.ascii_lowercase + string.digits, 8))
        email = random_str + "@gmail.com"
        email = "admin@coinbtc.us"
        input.send_keys(email)
        input.send_keys(Keys.RETURN)
    if i == 7 or i == 8:
        # 密码
        input.send_keys(pw)
        input.send_keys(Keys.RETURN)
    if i == 9:
        # 电话
        # input.send_keys("13612345678")
        input.send_keys("14782733578")
        input.send_keys(Keys.RETURN)
    if i == 14:
        # 验证码
        input.send_keys("ABCDEF")
        # input.send_keys(Keys.RETURN)
    i += 1


time.sleep(100)
driver.close()
