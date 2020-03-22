import tkinter
import tkinter.messagebox


def onClickTestBtn():
    tkinter.messagebox.askokcancel('提示','这是一个消息框')


main = tkinter.Tk()
main.geometry('800x400')

test_btn = tkinter.Button(main, text="Click", command=onClickTestBtn)
test_btn.pack()


main.mainloop()
