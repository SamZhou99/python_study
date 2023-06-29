import pyautogui as pyui
import time


def click():
    time.sleep(0.1)
    # pyui.moveTo(270, 360)
    # pyui.click()
    pyui.doubleClick()


sw, sh = pyui.size()
smx, smy = pyui.position()

time.sleep(5)
for i in range(1000):
    click()
