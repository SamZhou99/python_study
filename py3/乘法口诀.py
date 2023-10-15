def ChengFaKouJue():
    max_num = 9
    for i in range(1, max_num + 1):
        print()
        for j in range(1, i + 1):
            print("{}x{}={} ".format(i, j, i * j), end="")


def isFloat(num):
    return type(num) != int


def replaceAll(str):
    return replaceChat2(replaceChat1(str))


def replaceChat1(str):
    d = (
        str.strip()
        .replace("＝", "=")
        .replace("、", "")
        .replace("百万", "000000")
        .replace("千", "000")
        .replace("万", "0000")
        .replace("亿", "00000000")
    )
    return d


def replaceChat2(str):
    dd = (
        str.replace("＋", "+")
        .replace("－", "-")
        .replace("×", "*")
        .replace("÷", "/")
        # .replace("=", "")
    )
    return dd


def formatFloat(num):
    s = str(num)
    n1 = s.find(".")
    n2 = s[n1 + 1 :]
    l1 = len(str(n2))
    b1 = l1 >= 10
    if b1:
        return round(num, 6)
    if int(n2) > 0:
        # return "{} ?????????????? {} === {}".format(num, l1, int(n2))
        return num
    return int(num)


def calculator(equation):
    # print("计算")
    equation = equation.replace("=", "")
    equationRes = eval(equation)
    if isFloat(equationRes):
        return formatFloat(equationRes)
    else:
        return equationRes


import time


def formatOutput(arr):
    i = 0
    s = ""
    for item in arr:
        i = i + 1
        s = s + item + "\t"
        if i % 4 == 0:
            s = s + "\n"
    ts = time.strftime("%Y%m%d_%H%M%S")
    filename = "./计算结果_{}.txt".format(ts)
    print(filename)
    f = open(filename, "w", encoding="utf-8")
    f.write(s)

    # print(s)


def JiShuanTi():
    jst = """0÷3.5=	92÷4＝	0.6+5.47=	0.35+0.43=
15×4=	73＋15=	15×40=	15×8=
650÷5=	160×3=	720÷5＝	720÷4－135＝
120×600=	80－7×8=	13×2=	13×2=
19×7=	6000÷40=	200×30=	2.5÷0.5=
4.2×3=	36＋50=	4×25=	420÷3=
2.5÷5=	600×12=	200÷40=	20×5×6=
400×14=	3200＋4500=	400÷40=	48＋16=
15×5=	720÷48=	15×5=	150×2=
240×400=	51÷3=	26×30=	25＋68=
40×30=	3200×2=	400÷2=	47-27=
0.72÷0.6=	93÷31=	0.34÷17=	0.08+1.22=
15×5=	720÷60-8=	15×5=	150×5=
48÷7＝	270÷90＝	490÷70＝	50×70=
800÷4=	11×40＝	90－15=	910÷70=
8100－1900=	102×5=	93÷31＝	93÷31=
65×2=	160×4=	720÷4=	720÷4=
4×6＋8=	32－4×7=	40×800=	45÷7=
8400÷40=	10×47=	9900÷900=	900÷30=
64－36=	160×5=	720÷20÷2=	720÷4=
160×40=	68×101=	18×4=	18×4=
76－39=	12×8=	9.7-7=	90÷3="""
    row = jst.split("\n")
    index = 0
    arr = []
    for i in row:
        equationArr = i.split("\t")
        for item in equationArr:
            index = index + 1
            equationSource = replaceChat1(item)
            equationNew = replaceAll(item)
            equationResult = equationNew.split("=")[1]
            if equationResult == "":
                # print("{} {}{}".format(index, equationSource, calculator(equationNew)))
                arr.append("{}{}".format(equationSource, calculator(equationNew)))
            else:
                temp = calculator(equationNew.split("=")[0])
                if str(temp) == equationResult:
                    # print(index, equationSource)
                    arr.append(equationSource)
                else:
                    # print(index, equationSource, "\t\t【{}】".format(temp), "\txxxxxxxx")
                    arr.append("{} {}".format(equationSource, "xx"))
    formatOutput(arr)


# ChengFaKouJue()
JiShuanTi()
