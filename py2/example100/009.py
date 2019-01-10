#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 暂停下一秒输出 时间格式

import time

myD = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
}

for key, value in dict.items(myD):
    print key, value, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    time.sleep(1)  # 暂停 1 秒
