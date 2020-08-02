import tkinter
import tkinter.messagebox


def onClickTestBtn():
    tkinter.messagebox.askokcancel('提示','这是一个消息框')


main = tkinter.Tk()
main.geometry('800x400')

test_btn = tkinter.Button(main, text="Click Me", command=onClickTestBtn)
test_btn.pack(expand=1, fill='both')


main.mainloop()
