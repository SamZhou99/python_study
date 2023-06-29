import time


class EMailCode:
    def __init__(self) -> None:
        self.GET_URL = "http://149.28.74.54:8888/email/{}"
        # 间隔秒
        self.GET_STEP_TIME = 6
        # 重复请求最大次数
        self.GET_MAX_COUNT = 100

    def get(self, email):
        for i in range(self.GET_MAX_COUNT):
            time.sleep(self.GET_STEP_TIME)
            print(i + 1, "处理请求邮件数据", self.GET_URL.format(email))
            # 得到正确数据后，返回结果。（需要怎么判断，是正确的？）
            if True:
                return "返回正确数据"
        return "email code"
