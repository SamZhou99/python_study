import pyautogui
from timeit import default_timer as timer


startTime = timer()

# # 屏幕截图
# img = pyautogui.screenshot()  # x,y,w,h
# img.save('screenshot.png')


# # 返回真实的 图片 x,y,w,h
# findImgData = pyautogui.locateOnScreen('logo.png')
# print(findImgData)
# # 返回图片中心点坐标
# sx, sy = pyautogui.center(findImgData)
# print(sx, sy)


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
key_name = 'k'

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

pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
pyautogui.prompt('This lets the user type in a string and press OK.')

endTime = timer()
print('耗时:' + str(endTime - startTime))
