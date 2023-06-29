import random
from Paddle import Paddle
import tkinter
import tkinter.messagebox as mb
import tkinter


class Ball:
    def __init__(self, canvas: tkinter.Canvas, paddle: Paddle, tk: tkinter) -> None:
        self.tk = tk
        self.paddle = paddle
        self.speed = 1
        starts = [-3, -2, -1, 1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -self.speed
        self.canvas = canvas
        self.canvasHeight = canvas.winfo_height()
        self.canvasWidth = canvas.winfo_width()
        self.id = canvas.create_oval(0, 0, 30, 30, fill="#FF0000", outline="#FF0000")
        self.canvas.move(self.id, 50, 100)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # 边界判断
        # 上
        if pos[1] <= 0:
            self.y = self.speed
        # 下
        if pos[3] >= self.canvasHeight:
            self.y = 0
            mb.askokcancel("tip", "Game Over")
            self.tk.destroy()
            return
        # 左
        if pos[0] <= 0:
            self.x = self.speed
        # 右
        if pos[2] >= self.canvasWidth:
            self.x = -self.speed
        # 碰到木板反弹
        if self.hit_paddle(pos):
            self.y = -self.speed
            # 速度加快，增加难度
            self.speed += 1

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False
