import os, time, base64
import email
from datetime import datetime

dir_path = "./vmail/coinbtc.us/"
dir_path_username = []
dir_path_curr_eml = []
mail_admin = "1683943561.M401662P338478.mail.coinbtc.us,S=4395,W=4496"
mail_guest = "1683947662.M43866P343753.mail.coinbtc.us,S=4265,W=4364"
offset = 60 * 60 * 8


# 时间格式
def timeFormat(ts):
    # return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts))
    # 'Sat, 13 May 2023 10:05:55 +0800'
    GMT_FORMAT = "%a, %d %b %Y %H:%M:%S +0800"
    return datetime.strptime(ts, GMT_FORMAT)


# base64解码
def base64decode(txt, encode="utf-8"):
    return str(base64.b64decode(txt), encode)


def titleDecode(txt):
    title_length = len(txt)
    word_utf8 = "=?utf-8?B?"
    word_gbk = "=?gb18030?B?"
    word_len = len(word_gbk)
    if title_length < word_len:
        return txt, "gb18030"

    if txt[:word_len] == word_gbk:
        charset = word_gbk.replace("=?", "").replace("?B?", "")
        return base64decode(txt[word_len:], charset), charset

    word_len = len(word_utf8)
    if txt[:word_len] == word_utf8:
        charset = word_utf8.replace("=?", "").replace("?B?", "")
        return base64decode(txt[word_len:], charset), charset

    return txt, "gb18030"


def contentDecode():
    pass


# nextPart解析
def nextPartText(contentType):
    start_word = 'boundary="'
    start_index = contentType.find(start_word) + len(start_word)
    end_index = len(contentType) - 1
    next_part = contentType[start_index:end_index]
    return next_part


# nextPart具体内容
def nextPartContent(eml_code, next_part):
    next_part = "--" + next_part
    index = eml_code.find(next_part)
    word = "base64"
    start_index = eml_code.find(word, index + len(next_part))
    end_index = eml_code.find(next_part, start_index)
    return eml_code[start_index + len(word) : end_index]


# 读取eml
def readEML(eml_path):
    fp = open(eml_path, "r", errors="ignore")
    eml_code = fp.read()
    # return print(eml_code)
    msgs = email.message_from_string(eml_code)
    date = msgs["Date"]
    receiver_email = msgs["Delivered-To"]
    sender_email = msgs["Return-Path"]
    content_type = msgs["Content-Type"]
    title, charset = titleDecode(msgs["Subject"])
    next_part = nextPartText(content_type)
    content_txt = nextPartContent(eml_code, next_part)
    is_err = False
    try:
        content_txt = base64decode(content_txt, charset)
    except:
        is_err = True

    if is_err:
        print("还是错？？？", eml_path, title, charset)
        return

    print("\n时间：【{}】".format(timeFormat(date)))
    print("标题：【{}】".format(title))
    print("接收者：【{}】".format(receiver_email))
    print("发送者：【{}】".format(str(sender_email).replace("<", "").replace(">", "")))
    print("内容：【{}】".format(content_txt.strip().replace("\r\n", " ").replace("  ", "")))


# 读取用户路径
def accountDirPath():
    for username in dir_path_username:
        cur_eml_list = os.listdir(username + "cur")
        for i in range(len(cur_eml_list)):
            cur_eml_list[i] = username + "cur/" + cur_eml_list[i]

        new_eml_list = os.listdir(username + "new")
        for i in range(len(new_eml_list)):
            new_eml_list[i] = username + "new/" + new_eml_list[i]

        eml_list = []
        eml_list.extend(cur_eml_list)
        eml_list.extend(new_eml_list)
        eml_list.sort(reverse=True)

        for eml_path in eml_list:
            readEML(eml_path)
            break


# 读取数据路径
def dirPath():
    list = os.listdir(dir_path)
    for i in list:
        path = "{}{}/".format(dir_path, i)
        dir_path_username.append(path)


def init():
    dirPath()
    accountDirPath()


init()
