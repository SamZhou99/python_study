import os, time, base64, quopri
import email
from datetime import datetime


class VMail:
    def __init__(self) -> None:
        pass

    def latestEmails(self, domain, name):
        path = "./vmail/{}/{}/".format(domain, name)
        try:
            cur_eml_list = os.listdir(path + "cur")
        except:
            return {"err": "not found"}
        for i in range(len(cur_eml_list)):
            cur_eml_list[i] = path + "cur/" + cur_eml_list[i]

        try:
            new_eml_list = os.listdir(path + "new")
        except:
            return None
        for i in range(len(new_eml_list)):
            new_eml_list[i] = path + "new/" + new_eml_list[i]

        eml_list = []
        eml_list.extend(cur_eml_list)
        eml_list.extend(new_eml_list)
        if len(eml_list) <= 0:
            return {}

        eml_list.sort(reverse=True)

        for eml_path in eml_list:
            return readEML(eml_path)

        return None


offset = 60 * 60 * 8


# 时间格式
def timeFormat(ts):
    # return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts))
    # 'Sat, 13 May 2023 10:05:55 +0800'
    if ts.find("GMT") > 0:
        t = datetime.strptime(ts, "%a, %d %b %Y %H:%M:%S +0000 (GMT)").timestamp()
    else:
        t = datetime.strptime(ts, "%a, %d %b %Y %H:%M:%S +0800").timestamp()
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(t))


# base64解码
def base64decode(txt, charset="utf-8"):
    return str(base64.b64decode(txt), charset)


# quopri解码
def quopriDecode(txt, charset="gb2312"):
    print("【{}】".format(txt))
    return quopri.decodestring(txt).decode(charset)


# 标题解析
def titleDecode(txt):
    title_length = len(txt)
    word_utf8 = "=?utf-8?B?"
    word_gbk = "=?gb18030?B?"
    word_gb2312 = "=?gb2312?B?"
    word_len = len(word_gbk)
    if title_length < word_len:
        return txt, "gb18030"

    if txt[:word_len] == word_gbk:
        charset = word_gbk.replace("=?", "").replace("?B?", "")
        return base64decode(txt[word_len:], charset), charset

    word_len = len(word_gb2312)
    if txt[:word_len] == word_gb2312:
        charset = word_gb2312.replace("=?", "").replace("?B?", "")
        return base64decode(txt[word_len:], charset), charset

    word_len = len(word_utf8)
    if txt[:word_len] == word_utf8:
        charset = word_utf8.replace("=?", "").replace("?B?", "")
        return base64decode(txt[word_len:], charset), charset

    return txt, "gb18030"


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
    if eml_code.find(word) > 0:
        start_index = eml_code.find(word, index + len(next_part))
    elif eml_code.find("inline") > 0:
        start_index = eml_code.find("inline", index + len(next_part))
    end_index = eml_code.find(next_part, start_index)
    return eml_code[start_index + len(word) : end_index]


# 读取eml
def readEML(eml_path):
    fp = open(eml_path, "r", errors="ignore")
    eml_code = fp.read()
    # return print(eml_code)
    msgs = email.message_from_string(eml_code)
    date = msgs["Date"]
    ts = timeFormat(date)
    receiver_email = msgs["Delivered-To"]
    sender_email = msgs["Return-Path"]
    sender_email = sender_email.replace("<", "").replace(">", "")
    content_type = msgs["Content-Type"]
    title, charset = titleDecode(msgs["Subject"])
    next_part = nextPartText(content_type)
    content_txt = nextPartContent(eml_code, next_part)

    if sender_email.find("apple.com") > 0:
        # Content-Transfer-Encoding
        return {
            "ts": ts,
            "title": title,
            "content": quopriDecode(content_txt),
            "sender": sender_email,
            "receiver": receiver_email,
            "captcha": msgs["x-ds-vetting-token"],
        }

    is_err = False
    try:
        content_txt = base64decode(content_txt, charset)
    except:
        is_err = True

    if is_err:
        print("还是错？？？", eml_path, title, charset)
        return "Error", content_txt

    print("\n时间：【{}】".format(ts))
    print("标题：【{}】".format(title))
    print("接收者：【{}】".format(receiver_email))
    print("发送者：【{}】".format(sender_email))
    print("内容：【{}】".format(content_txt.strip().replace("\r\n", " ").replace("  ", "")))
    return {
        "ts": ts,
        "title": title,
        "content": content_txt,
        "sender": sender_email,
        "receiver": receiver_email,
    }
