import json


def check(word, list, start_index):
    for i in range(len(list) - start_index - 1):
        word1 = word.split("|")
        word1 = word1[1]
        word2 = list[start_index + i + 1].split("|")[1]
        if word1 == word2:
            return True
    return False


def difference():
    f = open("mail_format.txt", "r")
    t = f.read()
    l = t.split("\n")
    length = len(l)
    for i in range(length):
        if check(l[i], l, i):
            print(i, l[i])


def total():
    f = open("all_names.json", "r")
    t = f.read()
    o = json.loads(t)

    print(
        len(o["english"]),
        len(o["animal"]),
        len(o["plant"]),
        len(o["english"]) + len(o["animal"]) + len(o["plant"]),
    )


def init():
    domain = "@coinbtc.us"
    type_names = ["english", "animal", "plant"]
    f = open("all_names.json", "r")
    t = f.read()
    o = json.loads(t)
    # 名称|地址|密码|空间|单位
    # support|support@example.com.com|Password|5|GB
    # {}|{}|{}|5|GB
    for name in o["plant"]:
        print("{}|{}{}|{}|5|GB".format(name, name.lower(), domain, "aA123456"))


# init()

# difference()

total()
