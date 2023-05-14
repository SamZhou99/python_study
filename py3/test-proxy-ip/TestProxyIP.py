import requests


class TestProxyIP:
    # 开始测试
    def TestIp(self, proxy_ip):
        try:
            self.StartRequests(proxy_ip)
            return True
        except Exception as e:
            # print(str(e))
            return False

    # 谷歌浏览器
    def Headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }

    # 构建代理ip
    def Proxies(self, proxy_ip):
        return {
            "http": "http://" + proxy_ip,
            "https": "http://" + proxy_ip,
        }

    # 发起请求
    def StartRequests(self, proxy_ip):
        response = requests.get(
            url="https://api.coinbtc.us/api/test/ip",
            headers=self.Headers(),
            proxies=self.Proxies(proxy_ip),
            timeout=1,
        )  # 设置timeout，使响应等待1s
        print(response.json())
        response.close()
        if response.status_code == 200:
            print(proxy_ip, "\033[31m可用\033[0m")
            # 这里完成程序.............................
            return True
        else:
            print(proxy_ip, "不可用")
            return False
