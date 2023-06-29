import tkinter


class Paddle:
    def __init__(self, canvas: tkinter.Canvas) -> None:
        self.isMove = False
        self.speed = 5
        self.x = 0
        self.y = 0
        self.width = 100
        self.canvas = canvas
        self.canvasWidth = canvas.winfo_width()
        self.id = canvas.create_rectangle(0, 0, self.width, 10, fill="#FF0000")
        self.canvas.move(self.id, 0, canvas.winfo_height() - 60)
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] < 0:
            self.x = 1
            self.canvas.move(self.id, self.x, self.y)
            return

        if pos[2] > self.canvasWidth:
            self.x = -1
            self.canvas.move(self.id, self.x, self.y)
            return

        if self.isMove:
            self.canvas.move(self.id, self.x, self.y)
            # self.isMove = False

    def move_left(self, event):
        self.x = -self.speed
        self.isMove = True

    def move_right(self, event):
        self.x = self.speed
        self.isMove = True
