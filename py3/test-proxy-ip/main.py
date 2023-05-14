import requests
from lxml import etree
from TestProxyIP import TestProxyIP


all_ip_list = []  # 用于存放从网站上抓取到的ip
usable_ip_list = []  # 用于存放通过检测ip后是否可以使用


def request_header():
    headers = {
        # 谷歌浏览器
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    return headers


def send_request():
    # 爬取7页，可自行修改
    for i in range(1, 2):
        print(f"正在抓取第{i}页……")
        response = requests.get(
            url=f"http://www.ip3366.net/free/?page={i}", headers=request_header()
        )
        text = response.text.encode("ISO-8859-1")
        print(len(text.decode("gbk")))
        print(len(text))
        # 使用xpath解析，提取出数据ip，端口
        html = etree.HTML(text)
        print(len(html))
        tr_list = html.xpath("/html/body/div[2]/div/div[2]/table/tbody/tr")
        for td in tr_list:
            ip_ = td.xpath("./td[1]/text()")[0]  # ip
            port_ = td.xpath("./td[2]/text()")[0]  # 端口
            proxy = ip_ + ":" + port_  # 115.218.5.5:9000
            all_ip_list.append(proxy)
            # TestIp(proxy)  # 开始检测获取到的ip是否可以使用
            testIP = TestProxyIP()
            testIP.TestIp(proxy)
        print("抓取完成！")
        print(f"抓取到的ip个数为：{len(all_ip_list)}")
        print(f"可以使用的ip个数为：{len(usable_ip_list)}")
        print("分别有：\n", usable_ip_list)


def TestIp(proxy):
    # 构建代理ip
    proxies = {
        "http": "http://" + proxy,
        "https": "http://" + proxy,
    }
    try:
        response = requests.get(
            url="https://api.coinbtc.us/api/test/ip",
            headers=request_header(),
            proxies=proxies,
            timeout=1,
        )  # 设置timeout，使响应等待1s
        print(response.json())
        response.close()
        if response.status_code == 200:
            usable_ip_list.append(proxy)
            print(proxy, "\033[31m可用\033[0m")
            # 这里完成程序.............................
        else:
            print(proxy, "不可用")
    except:
        print(proxy, "请求异常")


def init():
    send_request()
    print("init")


init()
