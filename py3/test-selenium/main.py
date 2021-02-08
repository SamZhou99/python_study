from selenium import webdriver
import time
import requests


def login():
    driver.get(LOGIN_URL)
    driver.find_element_by_name("pwuser").clear()
    driver.find_element_by_name("pwuser").send_keys("ctrl999")
    driver.find_element_by_name("pwpwd").clear()
    driver.find_element_by_name("pwpwd").send_keys("aA123456")
    driver.find_element_by_name("submit").click()
    time.sleep(1)
    # cookies = driver.get_cookies()
    # print(cookies)
    # time.sleep(3)
    return (True)


def thread():
    driver.get(THREAD_URL)
    items = driver.find_elements_by_xpath("//table[@id='ajaxtable']/tbody/tr/td[2]/h3/a")
    print("len(item) = " + str(len(items)))
    a = []
    for i in items:
        t = {"title": i.text, "href": i.get_attribute("href")}
        print(t)
        a.append(t)
    time.sleep(1)
    return a


LOGIN_URL = "https://www.caecf5ca04934df3.xyz/login.php"
THREAD_URL = "https://www.caecf5ca04934df3.xyz/thread.php?fid=6&page=1"
# driver.get('https://www.caecf5ca04934df3.xyz/read.php?tid=207784')
driver = webdriver.Chrome()
login()
thread()
driver.quit()


# driver.quit()
# driver.find_element_by_id("id_name")
# driver.find_element_by_name("name")
# driver.find_element_by_tag_name("tag_name")
# driver.find_elements_by_class_name("class_name")
# driver.find_element_by_link_text("link_name")
# # <a href="http://www.google.com/search?q=cheese">search for cheese</a>>
# driver.find_element_by_partial_link_text("cheese")
# # css选择器示例
# driver.find_element_by_css_selector("#food span.dairy.aged")
# driver.find_element_by_css_selector(".s_ipt")