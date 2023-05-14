import os, time
import email

dir_path = "./vmail/coinbtc.us/"
dir_path_username = []
dir_path_curr_eml = []
mail_admin = "1683943561.M401662P338478.mail.coinbtc.us,S=4395,W=4496"
mail_guest = "1683947662.M43866P343753.mail.coinbtc.us,S=4265,W=4364"


def parseEML():
    pass


def readEML(path, eml):
    print(path, eml)


def getUserNameDirPath():
    for username in dir_path_username:
        path = username + "cur"
        eml_list = os.listdir(path)
        print("\n", username)
        offset = 60 * 60 * 8
        for eml in eml_list:
            t = eml.split(".")[0]
            t = int(t) + offset
            print("\t", t, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(t)))
            readEML(path, eml)


def getDirPath():
    list = os.listdir(dir_path)
    for i in list:
        path = "{}{}/".format(dir_path, i)
        dir_path_username.append(path)


def abc():
    fp = open(mail_admin, "r")
    msgs = email.message_from_file(fp)
    for par in msgs:
        print(par, msgs[par])


def init():
    getDirPath()
    getUserNameDirPath()


init()
