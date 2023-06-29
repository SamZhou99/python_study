def read(path):
    f = open(path, "r", encoding="utf-8")
    return f.read()


def write(path, text):
    f = open(path, "w", encoding="utf-8")
    return f.write(text)


def find(arr, short):
    for item in arr:
        li = item.split(" ")
        if li[0] == short:
            return li
    return False


apple_txt = read("./ApplePhoneShortName.txt")
aaa_txt = read("./aaa.txt")

apples = apple_txt.split("\n")
aaas = aaa_txt.split("\n")

i = 1
txt = ""
for item in apples:
    li = item.split(" ")
    short, zone, name = li[0], li[1], li[2]
    result = find(aaas, short)
    if result:
        # print(i, short, zone, name, result[2])
        txt += "{} {} {} {}\n".format(short, zone, name, result[2])
    i += 1
write("./ApplePhoneShortName_2.txt", txt)
