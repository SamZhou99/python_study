from PIL import Image
import matplotlib.pyplot as plt
import numpy as nps


# image = Image.open("./test.jpg")  # 读取图像
# plt.imshow(image) #显示图片

# plt.imshow(image.rotate(180))  #逆时针旋转180度
# plt.imshow(image.resize((64, 64)))  # 缩放


# # 转换灰度图像
# image_gray = image.convert('L')
# data = nps.array(image_gray)
# plt.imshow(image_gray)

# # 转换图像格式
# image.save('./test2.png')

# # 裁剪图片
# x, y = (300, 0)
# w, h = (600, 500)
# box = (x, y, x + w, y + h)
# region = image.crop(box)
# data = nps.array(region)
# plt.imshow(data)

# plt.show()  #需要调用show()方法，不然图像只会在内存中而不显示出来

from PIL import ImageDraw
import random

# from __future__ import division
import datetime
import pymysql
import time

config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "root",
    "db": "fer",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}
mysql_conn = pymysql.connect(**config)


def select(limit):
    sql = "SELECT * FROM kline_history WHERE symbol='{}' AND period='{}' ORDER BY id DESC LIMIT {}".format(
        "btcusdt", "30min", limit
    )
    print(sql)
    with mysql_conn.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()
        result_list = cursor.fetchall()
        for item in result_list:
            print(item["id"], item["close"] * 100)


def getMaxMinNum(res_list):
    max_num = res_list[0]["close"]
    min_num = max_num
    for i in res_list:
        num = i["close"]
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    return round(max_num, 2), round(min_num, 2)


step = 10
res_list = select(step)
maxNum, minNum = getMaxMinNum(res_list)
rangeNum = maxNum - minNum
print(maxNum, minNum, maxNum - minNum)
imgW = 100
imgH = 48
img = Image.new("RGB", color=0xFFFFFF, size=(imgW, imgH))
drawer = ImageDraw.Draw(img)
startX = 0
startY = (res_list[0]["close"] - minNum) / rangeNum * (imgH - 20) + 10
index = 1
for item in res_list:
    x2 = index * step
    y2 = (item["close"] - minNum) / rangeNum * (imgH - 20) + 10
    print(index, y2)
    drawer.line((startX, startY, x2, y2), fill="green", width=1)
    startX = x2
    startY = y2
    index = index + 1
index = 1
startX = 0
startY = 10
for item in res_list:
    x2 = index * step
    y2 = 10 + index
    drawer.line((startX, startY, x2, y2), fill="red", width=1)
    startX = x2
    startY = y2
    index = index + 1
img.save("./test-draw.png")
