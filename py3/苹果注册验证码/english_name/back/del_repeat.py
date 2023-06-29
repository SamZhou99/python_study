def init():
    type_name = "english"
    # type_name = "animal"
    # type_name = "plant"
    file_name = "./{}_names.txt".format(type_name)
    print(file_name)
    f = open(file_name, "r", encoding="utf-8")
    text = f.read()
    text_list = text.split("\n")

    # 排序
    text_list.sort()
    names = "\n".join(text_list)
    with open("./{}_names_2.txt".format(type_name), "w", encoding="utf-8") as fw:
        fw.write(names)

    # 去重
    len1 = len(text_list)
    list2 = list(set(text_list))
    len2 = len(list2)
    print(len1, len2)

    list2.sort()
    names = "\n".join(list2)

    with open("./{}_names_3.txt".format(type_name), "w", encoding="utf-8") as fw:
        fw.write(names)


init()
