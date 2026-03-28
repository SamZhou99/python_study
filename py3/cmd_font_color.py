import ctypes


STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_DARKBLUE = 0x01  # 暗蓝色
FOREGROUND_DARKGREEN = 0x02  # 暗绿色
FOREGROUND_DARKSKYBLUE = 0x03  # 暗天蓝色
FOREGROUND_DARKRED = 0x04  # 暗红色
FOREGROUND_DARKPINK = 0x05  # 暗粉红色
FOREGROUND_DARKYELLOW = 0x06  # 暗黄色
FOREGROUND_DARKWHITE = 0x07  # 暗白色
FOREGROUND_DARKGRAY = 0x08  # 暗灰色
FOREGROUND_BLUE = 0x09  # 蓝色
FOREGROUND_GREEN = 0x0A  # 绿色
FOREGROUND_SKYBLUE = 0x0B  # 天蓝色
FOREGROUND_RED = 0x0C  # 红色
FOREGROUND_PINK = 0x0D  # 粉红色
FOREGROUND_YELLOW = 0x0E  # 黄色
FOREGROUND_WHITE = 0x0F  # 白色

D_COLOR = {
    "暗天蓝": FOREGROUND_DARKSKYBLUE,
    "暗蓝": FOREGROUND_DARKBLUE,
    "暗绿": FOREGROUND_DARKGREEN,
    "暗红": FOREGROUND_DARKRED,
    "暗粉": FOREGROUND_DARKPINK,
    "暗黄": FOREGROUND_DARKYELLOW,
    "暗白": FOREGROUND_DARKWHITE,
    "暗灰": FOREGROUND_DARKGRAY,
    "天蓝": FOREGROUND_SKYBLUE,
    "蓝": FOREGROUND_BLUE,
    "绿": FOREGROUND_GREEN,
    "红": FOREGROUND_RED,
    "粉": FOREGROUND_PINK,
    "黄": FOREGROUND_YELLOW,
    "白": FOREGROUND_WHITE,
}

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    return ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)


def set_text_color(name):
    color = D_COLOR.get(name, FOREGROUND_WHITE)
    set_cmd_text_color(color)


def reset_color():
    set_cmd_text_color(FOREGROUND_DARKWHITE)


def cprint(text, color):
    set_text_color(color)
    print(text)
    reset_color()


if __name__ == "__main__":
    for k in D_COLOR:
        cprint(f"我是{k}色文字", k)
    set_text_color("天蓝")
    print("-" * 30)
    input("It's interesting, right?")
    reset_color()
