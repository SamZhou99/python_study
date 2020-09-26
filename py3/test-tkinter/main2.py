import tkinter
import tkinter.messagebox


def onClickTestBtn():
    tkinter.messagebox.askokcancel('提示', '这是一个消息框')
    text.set('点击了按钮')


fontName = "微软雅黑"
fontSize = 32

main = tkinter.Tk()
main.geometry('800x400')

text = tkinter.StringVar()
text.set('change to what?')
entry = tkinter.Entry(main, font=(fontName, fontSize))
entry['textvariable'] = text
entry.pack()

test_btn = tkinter.Button(main, text="Click Me",
                          command=onClickTestBtn, font=(fontName, fontSize))
test_btn.pack(expand=1, fill='both')

main.mainloop()
