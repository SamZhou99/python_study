import ctypes
import time

delay_time = 5

try:
    delay_time = int(input('请输入数字(默认5秒)：'))
except ValueError:
    print('参数没有包含数字', ValueError)

time.sleep(delay_time)

ctypes.windll.user32.LockWorkStation()
