# encoding:utf-8
import math
import re


def cost01(duration):
    # 60秒,1分鐘
    time = 60
    # 1.2元
    price = 1.2
    resTime = math.ceil(float(duration) / float(time))
    return (resTime, resTime * price)


duration = int(re.sub('\D', '', raw_input('输入时长(秒):\n')))

r, p = cost01(duration)

print(str(duration)+'m', str(r) + 'm', str(p) + 'rmb')
