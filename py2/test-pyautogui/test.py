#!/usr/bin/env python
# coding=utf-8
import pyautogui
import math

# pyautogui.PAUSE = 0.25
pyautogui.FAILSAFE = True
# 屏幕寬高
width, height = pyautogui.size()
# 鼠標座標
x, y = pyautogui.position()


def drawRectangle():
    for i in range(3):
        d = 0.15
        pyautogui.moveTo(300, 300, duration=d)
        pyautogui.moveTo(400, 300, duration=d)
        pyautogui.moveTo(400, 400, duration=d)
        pyautogui.moveTo(300, 400, duration=d)


def drawCircle():
    r = 250  # 圆的半径
    # 圆心
    o_x = width/2
    o_y = height/2

    pi = 3.1415926

    for i in range(3):
        for angle in range(0, 360, 5):  # 利用圆的参数方程
            X = o_x + r * math.sin(angle*pi/180)
            Y = o_y + r * math.cos(angle*pi/180)

            pyautogui.moveTo(X, Y, duration=0.1)


def moveRel():
    for i in range(10):
        # 相对坐标
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)


def imgScreenshot():
    im = pyautogui.screenshot()
    # 获得某个坐标的像素
    im.getpixel((50, 200))
    # (30, 132, 153)
    # 判断屏幕坐标的像素是不是等于某个值
    pyautogui.pixelMatchesColor(50, 200, (30, 132, 153))
    pyautogui.locateOnScreen('button.png')
    x, y = pyautogui.center((643, 745, 70, 29))  # 获得中心点
    pyautogui.click(x, y)


drawRectangle()
# drawCircle()
# pyautogui.rightClick()
# pyautogui.doubleClick
# pyautogui.click(100, 100)
# pyautogui.click(x=cur_x, y=cur_y, button='left')
# 鼠標拖動
# pyautoguidragTo() 和 pyautoguidragRel()
# 滾輪
# pyautogui.scroll(200)
# pyautogui.typewrite('Hello world!', 0.1)
# pyautogui.typewrite(['enter', 'a', 'b', 'left', 'left', 'X', 'Y'], '0.25')


# pyautogui.hotkey('altleft', 'f4')
pyautogui.hotkey('shiftleft', 'f5', 2)















# # 1 安装pyautuogui
# # pip install pyautogui

# # 2 鼠标控制常用命令
# import pyautogui
# pyautogui.PAUSE = 1  # 每次pyautogui后的等待时间
# pyautogui.FAILSAFE = True  # 自动防故障功能开启，将鼠标移到屏幕的左上角可停用代码

# pyautogui.moveTo(100,200,duration=1)  # 移动鼠标到指定位置（绝对位置），duration为移动时间
# pyautogui.moveRel(10,20,duration=1)  # 移动鼠标到指定位置（相对位置），duration为移动时间

# x,y = pyautogui.size()  # 获取屏幕的分辨率
# x,y = pyautogui.position()  # 获取鼠标的位置

# pyautogui.mouseDown()  # 按下鼠标按键
# pyautogui.mouseUp()  # 释放鼠标按键
# pyautogui.click()  # 点击鼠标，相当于按下和释放的封装组合

# pyautogui.dragTo(100,200,duration=1)  # 拖动鼠标到指定位置（绝对位置），duration为移动时间
# pyautogui.moveRel(10,20,duration=1)  # 拖动鼠标到指定位置（相对位置），duration为移动时间

# pyautogui.scroll()  # 滚动鼠标

# im = pyautogui.screenshot()  # 获取屏幕快照
# im.getpixel((100,200))  # 返回坐标处的像素颜色，即RGB（红绿蓝）值
# pyautogui.pixelMatchesColor(50,200,(130,135,144))  # 将屏幕上指定的x，y坐标处的像素与指定的颜色匹配

# list(pyautogui.locateAllOnScreen('png.png'))  # 获取png图片的位置，如果找到多个则默认返回一个list元组，如(643,745,70,29)，分别为图像左边的X坐标，顶边的Y坐标，宽度，以及高度
# pyautogui.locateOnScreen('png.png')  # 获取图片的位置，结果如(643,745,70,29)
# pyautogui.center((643,745,70,29))  # 获取中心值，结果如(678,759)


# # 3 键盘控制常用命令
# pyautogui.typewrite('Hello World',0.25)  # 打印出相应字符串，后面的时间为打印后等待的时间

# pyautogui.keyDown()  # 按下按键
# pyautogui.keyUp()  # 释放按键
# pyautogui.press()  # 点击按键，相当于按下和释放的集合

# pyautogui.hotkey('Ctrl','c')  # 热键组合，可以接受多个按键字符串参数，顺序按下，再按相反的顺序释放

# pyautogui.KEYBOARD_KEYS  # 查看PyKeyboard属性值