import json


def init():
    obj = {}
    type_names = ["english", "animal", "plant"]
    for type in type_names:
        f = open("./{}_names.txt".format(type), "r", encoding="utf-8")
        t = f.read()
        obj[type] = t.split("\n")

    fw = open("./all_names.json", "w", encoding="utf-8")
    fw.write(json.dumps(obj))


init()
