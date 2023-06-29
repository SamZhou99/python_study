def read(path):
    f = open(path, "r", encoding="utf-8")
    return f.read()


def write(path, text):
    f = open(path, "w", encoding="utf-8")
    return f.write(text)


def find(countrys, cn, en):
    for item in countrys:
        li = item.split(" ")
        if li[2] == cn:
            return li
        if li[1] == en:
            return li
    return False


apple_txt = read("./ApplePhoneShortName_2.txt")
phone_country_txt = read("./SmsActivateCountryID.txt")

apples = apple_txt.split("\n")
phone_countrys = phone_country_txt.split("\n")

i = 1
txt = ""
for item in apples:
    li = item.split(" ")
    short, zone, name, en = li[0], li[1], li[2], li[3]
    result = find(phone_countrys, name, en)
    if result:
        print(short, zone, name, en, result[0], result[1])
        txt += "{} {} {} {} {}\n".format(short, zone, name, result[0], result[1])
    i += 1
write("./AppleCountry_2.txt", txt)
