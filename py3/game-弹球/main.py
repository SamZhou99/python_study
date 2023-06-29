import tkinter

# from tkinter import *
import tkinter.messagebox as mb
import time

from Ball import Ball
from Paddle import Paddle

tk = tkinter.Tk()
canvas = None
canvas_width = 600
canvas_hight = 500


def callback():
    # Ball.flag = False
    mb.askokcancel("提示", "这是一个消息框")
    tk.destroy()


def initTK():
    tk.title("小弹球游戏V1版")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    # tk.protocol("WM_DELETE_WINDOW", callback)


def initCanvas():
    global tk, canvas, canvas_width, canvas_hight
    canvas = tkinter.Canvas(
        tk,
        width=canvas_width,
        height=canvas_hight,
        bd=0,
        highlightthickness=0,
        bg="#222222",
    )
    canvas.pack()
    tk.update()


def main():
    initTK()
    initCanvas()

    global tk, canvas, ball
    paddle = Paddle(canvas)
    ball = Ball(canvas, paddle, tk)

    while True:
        tk.update_idletasks()
        tk.update()
        ball.draw()
        paddle.draw()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
