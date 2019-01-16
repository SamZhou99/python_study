# encoding:utf-8
import math


def cost01(duration):
    # 60秒,1分鐘
    time = 60
    # 1.2元
    price = 1.2
    resTime = math.ceil(float(duration) / float(time))
    return (resTime, resTime * price)


duration = int(raw_input('输入时长(秒):\n'))

r, p = cost01(duration)

print(str(r) + 'm', str(p) + 'rmb')
