from selenium import webdriver
import time
import requests
import data

# POST_URL = 'http://www.lajiao999.com/admin/article'
POST_URL = 'http://127.0.0.1:3000/admin/article'
# SITE_URL = 'https://www.caecf5ca04934df3.xyz'
# SITE_URL = 'https://cl260d.com'
# SITE_URL = 'https://cl34ce.com'
SITE_URL = 'https://cl6371.com'
SITE_CODE = 'caoliu1024'
LOGIN_URL = SITE_URL + '/login.php'
THREAD_URL = SITE_URL + '/thread.php?fid={fid}&page={page}'
DATA_FILE_NAME = 'data.txt'
THREAD_LIST = [
    {
        'fid': 33,
        'name': 'VIP影视区',
        'page': 5
    },
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
chrome_options.set_headless()
# 不加载 IMG 和 JS, CSS
chrome_options.add_experimental_option('prefs', {'profile.default_content_setting_values': {'images': 2, 'javascript': 2, 'permissions.default.stylesheet': 2}})
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_page_load_timeout(30)

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


# 某个类型 列表，返回 title, href
def getThreadList(page=1):
    fid = THREAD_LIST[thread_index]['fid']
    page_url = THREAD_URL.replace('{fid}', str(fid)).replace('{page}', str(page))
    print('分类列表：{}'.format(page_url))
    get(page_url)
    items = driver.find_elements_by_xpath("//table[@id='ajaxtable']/tbody/tr/td[2]/h3/a")
    print('分类列表有 {} 条'.format(str(len(items))))
    a = []
    for i in items:
        if i.get_attribute('innerHTML').find('blue') == -1:
            t = {'title': i.text, 'href': i.get_attribute('href')}
            a.append(t)
    time.sleep(1)
    return a


# 获取正文内容 playUrl, imgTxt
def getContentPage(url):
    print('打开内容页面URL：{}'.format(url))
    get(url)
    playUrl = driver.find_element_by_link_text('點擊這里打開新視窗').get_attribute('href')
    imgTxt = driver.find_element_by_xpath("//div[@id='idstpc']/img").get_attribute('data-aes')
    if (playUrl):
        n1 = playUrl.rfind('&rnd')
        playUrl = playUrl[:n1]
    if (not imgTxt):
        imgTxt = '/img/default-item-bg-01.jpg'
    time.sleep(1)
    return playUrl, imgTxt


# 获取m3u8地址
def getPlayPage(playUrl):
    print('视频播放的URL：{}'.format(playUrl))
    get(playUrl)
    html = driver.page_source
    n1 = html.find('m3u8')
    n2 = html.rfind("'", 0, n1 - 1)
    n3 = html.find("'", n1 + 1)
    m3u8_url = html[n2 + 1:n3]
    print('m3u8地址：{}'.format(m3u8_url))
    return m3u8_url


# 提交数据到远程
def post_data(item):
    data = {
        'title': item['title'],
        'type1': THREAD_LIST[thread_index]['name'],
        'type2': '草榴社区',
        'img': item['imgTxt'],
        'link': item['playUrl'],
        'source_site': SITE_CODE,
        'video': item['m3u8'],
        'status': 1,
        'play_type': 'm3u8',
        'date': dateTime(),
        'created': dateTime()
    }
    print('要提交的数据')
    print(data)
    requests.post(POST_URL, data=data)
    print()
    time.sleep(1)


# 开始获取
def start():
    for index in range(len(THREAD_LIST)):
        print('{}, {}, {}'.format(index, THREAD_LIST[index]['fid'], THREAD_LIST[index]['name']))
        page_max = THREAD_LIST[index]['page']
        for page in range(page_max):
            threadList = getThreadList(page_max - page)
            i = 0
            for item in threadList:
                i = i + 1
                url = item['href']
                print('开始第 {} 条数据'.format(i))
                try:
                    item['playUrl'], item['imgTxt'] = getContentPage(url)
                    item['m3u8'] = getPlayPage(item['playUrl'])
                    post_data(item)
                except:
                    print('❌打开页面异常 URL：{}'.format(url))
                    print('解析异常')
                # break
            # break


# 初始化
def init():
    loginRes = login('ctrl999', 'aA123456')
    if loginRes:
        start()
    driver.quit()


init()
