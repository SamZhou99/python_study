import requests
from lxml import etree
from proxy_ip.TestProxyIP import TestProxyIP


def getPageHtml(url):
    resp = requests.get(url)
    text = resp.text.encode("ISO-8859-1")
    # print(text.decode("gbk"))
    return text.decode("gbk")


def checkValType(val):
    try:
        int(val)
        return True
    except:
        return False


def parseHtml(text):
    ip_list = []
    html = etree.HTML(text)
    # print(len(html))
    tr_list = html.xpath(
        "/html/body/div[@id='main']/div[@class='containerbox boxindex']/div[@class='layui-row layui-col-space15']/div[1]/table/tr"
    )
    # print(tr_list)
    for td in tr_list:
        ip = td.xpath("./td[1]/text()")[0]  # ip
        port = td.xpath("./td[2]/text()")[0]  # 端口
        proxy = ip + ":" + port
        if checkValType(ip[0]) and checkValType(proxy[0]):
            ip_list.append(proxy)
    return ip_list


def init():
    for i in range(3):
        url = "http://www.66ip.cn/{}.html".format(i + 1)
        text = getPageHtml(url)
        ip_list = parseHtml(text)
        print(ip_list)
        for ip in ip_list:
            testProxyIP = TestProxyIP()
            print(testProxyIP.TestIp(ip), ip)


init()
# ip = "38.41.29.78:8080"
# testProxyIP = TestProxyIP()
# print(testProxyIP.TestIp(ip), ip)
