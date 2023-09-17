import pyautogui
from timeit import default_timer as timer


startTime = timer()


def screenshot():
    # 屏幕截图
    # w, h = 3840, 2160
    w, h = 800, 600
    img = pyautogui.screenshot(region=(0, 0, w, h))  # x,y,w,h
    img.save("screenshot-2.png")


def imgInfo():
    # 返回真实的 图片 x,y,w,h
    findImgData = pyautogui.locateOnScreen("logo.png")
    print(findImgData)
    # 返回图片中心点坐标
    sx, sy = pyautogui.center(findImgData)
    print(sx, sy)


def mouseAct():
    curr_mouse_xy = pyautogui.position()
    print(curr_mouse_xy)

    screen_resolution = pyautogui.size()
    print(screen_resolution)

    num_seconds = 1
    x = 1000
    y = 100
    xOffset = 100
    yOffset = 100
    num_of_clicks = 10
    secs_between_clicks = 10
    secs_between_keys = 0.1
    moveToX = 200
    moveToY = 200
    amount_to_scroll = -10
    key_name = "k"

    screen = pyautogui.onScreen(x, y)
    print(screen)

    pyautogui.moveTo(x, y, duration=num_seconds)
    # pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)

    # pyautogui.click(x=xOffset, y=xOffset, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
    # pyautogui.rightClick(x=moveToX, y=moveToY)
    # pyautogui.middleClick(x=moveToX, y=moveToY)
    # pyautogui.doubleClick(x=moveToX, y=moveToY)
    # pyautogui.tripleClick(x=moveToX, y=moveToY)

    # pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)

    # pyautogui.dragTo(xOffset, yOffset, duration=num_seconds)
    # pyautogui.dragRel(xOffset+100, yOffset+100, duration=num_seconds)

    # pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)

    # pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
    # pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste

    # pyautogui.keyDown(key_name)
    # pyautogui.keyUp(key_name)


def alertModel():
    pyautogui.alert("This displays some text with an OK button.")
    pyautogui.confirm("This displays text and has an OK and Cancel button.")
    pyautogui.prompt("This lets the user type in a string and press OK.")


def isFloat(n):
    return isinstance(n, float)


def isInt(n):
    return isinstance(n, int)


def getScale(w, h):
    len = w if w > h else h
    i = 0
    while len > 0:
        i = i + 1
        ww = w / len
        hh = h / len
        len = len - 1
        if ww == int(ww) and hh == int(hh):
            print(i, "计算次数")
            return int(ww), int(hh)
    return 0, 0


def getScale2(w, h):
    i = 0
    isZ = w > h
    W, H = (w, h) if isZ else (h, w)
    w, h = W, H
    while i < 10:
        i = i + 1
        m = w % h
        print(i, w, h, m)
        if m == 0:
            return (int(W / h), int(H / h)) if isZ else (int(H / h), int(W / h))
        else:
            w = h
            h = m
    return 0


# screenshot()


# print(getScale2(3840, 2160))
# print(getScale2(1024, 768))
print(getScale2(15563, 19109))


endTime = timer()
print("耗时:" + str(endTime - startTime))
