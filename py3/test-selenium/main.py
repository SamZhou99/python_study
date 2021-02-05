from selenium import webdriver
import time
import requests

driver = webdriver.Chrome()

# driver.get('https://www.caecf5ca04934df3.xyz/read.php?tid=207784')
driver.get('https://www.caecf5ca04934df3.xyz/login.php')
driver.find_element_by_name("pwuser").clear()
driver.find_element_by_name("pwuser").send_keys("ctrl999")
driver.find_element_by_name("pwpwd").clear()
driver.find_element_by_name("pwpwd").send_keys("aA123456")
driver.find_element_by_name("submit").click()
time.sleep(3)

cookies = driver.get_cookies()
print(cookies)
time.sleep(3)


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