from tkinter import Tk
from tkinter import Button
import Common


def hi():
    print('hello')


def quit():
    root.destroy()


root = Tk()
root.title('窗口标题')
root.geometry('1000x500')
root.config(bg=Common.Style.bg())

btn1 = Button(root, text='TestButton', command=hi, font=Common.Style.font(), bg=Common.Style.bg())
btn1.pack()

btnQuit = Button(root, text='Quit', command=quit, font=Common.Style.font(), bg=Common.Style.bg())
btnQuit.pack()

root.mainloop()
