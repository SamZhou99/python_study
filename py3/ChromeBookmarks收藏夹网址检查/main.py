import requests
import time, json


# for folder in chrome_bookmarks.folders:
#     print(folder.name)
#     print(folder.folders)
# for url in chrome_bookmarks.urls:
#     print(url.url, url.name)


def read(file):
    f = open(file, encoding="utf-8")
    return f.read()


def write(file, str):
    f = open(file, encoding="utf-8", mode="w")
    f.write(str)
    return True


def testUrl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    }
    try:
        res = requests.get(url, headers=header, timeout=3)
        if res.status_code == 200:
            return ("ok", url)
        else:
            return ("err", url)
    except:
        return ("err", url)


def loopList(child, index):
    for item in child["children"]:
        if item["type"] == "folder":
            continue
        time.sleep(1)
        res, url = testUrl(item["url"])
        if res == "ok":
            print("{}\tok\t\t{}\t\t{}".format(index, item["name"], url))
        else:
            item["name"] = "X_" + item["name"]
            print("{}\terr\t\t{}\t\t{}".format(index, item["name"], url))


def saveFile(fill_name, obj):
    txt2 = json.dumps(obj, ensure_ascii=False)
    write(fill_name + "_2", txt2)


# testUrl("https://www.baidu0.com")
dir_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/Default/"
file_name = "Bookmarks"
fill_name = dir_path + file_name

txt = read(fill_name)
obj = json.loads(txt)

index = 0
for child in obj["roots"]["other"]["children"]:
    index += 1
    if index <= 4:
        continue
    if child == None:
        continue
    if child.get("children") == None:
        continue

    try:
        loopList(child, index)
    except:
        saveFile(fill_name, obj)
    # break

saveFile(fill_name, obj)

# for child in obj["roots"]["other"]["children"]:
#     for item in child["children"]:
#         res, url = testUrl(item["url"])
#         if res == "ok":
#             print("ok", url)
#         else:
#             print("err", item["name"], url)
#     break
print("ok")
