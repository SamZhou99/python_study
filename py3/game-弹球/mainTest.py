import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=2000, height=400)
canvas.pack()

circle = canvas.create_oval(100, 100, 150, 150, fill="red")


def move():
    canvas.move(circle, 10, 0)
    canvas.update()  # 关键：强制立即刷新
    root.after(5, move)


move()
root.mainloop()
