def isChinese(chars):
    if "\u4e00" <= chars <= "\u9fff":
        return True
    else:
        return False


def indexOfChineseWord(word):
    i = 0
    for c in word:
        if isChinese(c):
            return i
        i += 1
    return -1


def readNames(text):
    res = ""
    text_list = text.split("\n")
    for t in text_list:
        t = t.strip()
        if t:
            i = indexOfChineseWord(t)
            name = t[:i]
            name = name.strip()
            if name:
                if name.find("/") > 0:
                    names = name.split("/")
                    for n in names:
                        if n.strip():
                            # 修剪完的
                            res = "{}\n{}".format(res, n)
                elif not (
                    name.find(",") > 0
                    or name.find(" ") > 0
                    or name.find("，") > 0
                    or name.find("-") > 0
                ):
                    # 原本合格的
                    res = "{}\n{}".format(res, name)
    return res


def init():
    type_name = "english"
    type_name = "animal"
    type_name = "plant"

    f = open("./{}_name.txt".format(type_name), "r", encoding="utf-8")
    text = f.read()
    names = readNames(text)

    with open("./{}_names.txt".format(type_name), "w", encoding="utf-8") as fw:
        fw.write(names)


init()
