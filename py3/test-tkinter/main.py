# import tkinter
from tkinter import *
import tkinter.messagebox
import random
import math
import time

# def onClickTestBtn():
#     tkinter.messagebox.askokcancel('提示', '这是一个消息框')
#     resultText.set('点击了按钮')
# testBtn = tkinter.Button(main, text="Click Me",
#                          command=onClickTestBtn, font=defaultFontStyle)
# testBtn.grid(row=1, column=9)


def handlerAdaptor(fun, **kwds):
    # 事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧
    return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


def getRandom(minNum, maxNum):
    return minNum + math.ceil(random.random() * (maxNum - minNum))


def focus_cg(event, e2):
    titleText.set(str(getRandom(minNum, maxNum)))
    print(resultText.get())
    # e2.focus_set()  # 焦点移到e2


titleFontStyle = ("Courier Prime", 32)
infoFontStyle = ("Courier Prime", 18)
defaultFontStyle = ("Courier Prime", 64)
stageWidth = 800
stageHeight = 400
questionNum = 10
questionIndex = 0
minNum = 10
maxNum = 99

main = tkinter.Tk()
main.geometry(str(stageWidth) + "x" + str(stageHeight))
# 标题
titleText = tkinter.StringVar()
titleText.set('100以内 计算题')
titleLabel = tkinter.Label(main, textvariable=titleText, font=titleFontStyle)

# 提示信息
infoText = tkinter.StringVar()
infoText.set('共{}题, 当前{}题'.format(str(questionNum), str(questionIndex)))
infoLabel = tkinter.Label(main, textvariable=infoText, font=infoFontStyle)

# 第一个数
n1Label = tkinter.Label(main,
                        text="0",
                        width=2,
                        bg="#EEEEEE",
                        font=defaultFontStyle)

# 运算符号
symbol1Label = tkinter.Label(main,
                             text="+",
                             width=1,
                             bg="#EEEEEE",
                             font=defaultFontStyle)

# 第二个数
n2Label = tkinter.Label(main,
                        text="0",
                        width=2,
                        bg="#EEEEEE",
                        font=defaultFontStyle)

# 等于符号
symbol2Label = tkinter.Label(main,
                             text="=",
                             width=1,
                             bg="#EEEEEE",
                             font=defaultFontStyle)

# 运算结果
resultText = tkinter.StringVar()
resultText.set("?")
resultEntry = tkinter.Entry(main, width=3, bg="red", font=defaultFontStyle)
resultEntry["textvariable"] = resultText
resultEntry.bind("<Return>", handlerAdaptor(focus_cg, e2=resultEntry))

# 布局
titleLabel.grid(row=0, column=0, columnspan=100, sticky=W)
infoLabel.grid(row=1, column=0, columnspan=100, sticky=W)
n1Label.grid(row=2, column=0)
symbol1Label.grid(row=2, column=1)
n2Label.grid(row=2, column=2)
symbol2Label.grid(row=2, column=3)
resultEntry.grid(row=2, column=4)

resultEntry.focus_set()

main.mainloop()
