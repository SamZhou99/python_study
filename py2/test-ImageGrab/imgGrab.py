#!/usr/bin/env python
# coding=utf-8
from PIL import ImageGrab, Image
# pip install Pillow
import zlib
import time
import threading


def saveImg():
    imgType = 'jpeg'
    extName = 'jpg'
    timeStr = time.strftime("%Y%m%d%H%M%S", time.localtime())
    imgFile = './'+timeStr+'.'+extName
    # im = ImageGrab.grab((483, 225, 883, 525))
    img = ImageGrab.grab()
    # Image.BILINEAR
    # Image.BICUBIC
    # Image.ANTIALIAS
    img = img.resize((1600, 900), Image.ANTIALIAS)
    # img.save(imgFile, imgType, quality=50)

    # zlib壓縮
    imgBytes = img.tobytes()
    print('imgBytes', len(imgBytes))
    compressedBytes = zlib.compress(imgBytes)
    print('compressedBytes', len(compressedBytes))
    img2 = Image.frombytes('RGB', img.size, zlib.decompress(compressedBytes))
    img2.save(imgFile, imgType, quality=50)
    print(imgFile)

    timer = threading.Timer(1, saveImg)
    timer.start()


saveImg()
