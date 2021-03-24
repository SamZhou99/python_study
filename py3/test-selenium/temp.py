# driver.quit()
# driver.find_element_by_id('id_name')
# driver.find_element_by_name('name')
# driver.find_element_by_tag_name('tag_name')
# driver.find_elements_by_class_name('class_name')
# driver.find_element_by_link_text('link_name')
# # <a href='http://www.google.com/search?q=cheese'>search for cheese</a>>
# driver.find_element_by_partial_link_text('cheese')
# # css选择器示例
# driver.find_element_by_css_selector('#food span.dairy.aged')
# driver.find_element_by_css_selector('.s_ipt')
# driver.get('https://www.caecf5ca04934df3.xyz/read.php?tid=207784')
# cookies = driver.get_cookies()
# print(cookies)
# time.sleep(3)

# dict = {'title': "标题", "age": 23}
# print(dict["title"])
# print(type(dict))
# print(str(dict))

# for i in range(3, 9):
#     print(i)

# str = "abcdefghijklmnopqrstuvwxycz"
# substr = "c"
# print(str.rfind(substr, 0, 10))

# import time
# t = time.localtime()
# print("{}-{}-{} {}:{}:{}".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))
# print(time.mktime(time.localtime()))
# print(time.time())

# a = 1
# b = 2
# def swp(a, b):
#     return b, a
# a, b = swp(a, b)
# print(a, b)

# for i in range(10):
#     print(10 - i)

# def fibonacci(num):
#     n1 = 0
#     n2 = 1
#     for i in range(num):
#         n3 = n1 + n2
#         n1, n2 = n2, n3
#         print('{}:{}'.format(i, n3))

# fibonacci(10)





from selenium import webdriver
import time
import requests
import data

POST_URL = 'http://www.lajiao999.com/admin/article'
# SITE_URL = 'https://www.caecf5ca04934df3.xyz'
SITE_URL = 'https://cl260d.com'
SITE_CODE = 'caoliu1024'
LOGIN_URL = SITE_URL + '/login.php'
THREAD_URL = SITE_URL + '/thread.php?fid={fid}&page={page}'
DATA_FILE_NAME = 'data.txt'
THREAD_LIST = [
    {
        'fid': 6,
        'name': '国产原创',
        'page': 18
    },
    {
        'fid': 7,
        'name': '中文字幕',
        'page': 17
    },
    {
        'fid': 2,
        'name': '亚洲无码',
        'page': 22
    },
    {
        'fid': 3,
        'name': '亚洲有码',
        'page': 15
    },
    {
        'fid': 4,
        'name': '欧美原创',
        'page': 10
    },
]
thread_index = 2

chrome_options = webdriver.ChromeOptions()
# 无界面
# chrome_options.set_headless()
# 不加载 IMG 和 JS, CSS
# chrome_options.add_experimental_option('prefs', {'profile.default_content_setting_values': {'images': 2, 'javascript': 2, 'permissions.default.stylesheet': 2}})
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_page_load_timeout(5)

# driver.manage().timeouts().setScriptTimeout(3,TimeUnit.SECONDS);


# 日期时间格式
def dateTime():
    t = time.localtime()
    return '{}-{}-{} {}:{}:{}'.format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)


def get(url):
    for i in range(6):
        try:
            driver.get(url)
            break
        except:
            pass
        # continue
    return i


# 登录
def login(user_name, password):
    print('登录页：{}'.format(LOGIN_URL))
    get(LOGIN_URL)
    driver.find_element_by_name('pwuser').clear()
    driver.find_element_by_name('pwuser').send_keys(user_name)
    driver.find_element_by_name('pwpwd').clear()
    driver.find_element_by_name('pwpwd').send_keys(password)
    driver.find_element_by_name('submit').click()
    time.sleep(1)
    return (True)



get('https://s.taobao.com/search?spm=a21bo.2017.201867-links-0.15.5af911d9HFlLtM&q=%E8%BF%9E%E8%A1%A3%E8%A3%99%E5%A5%B3')