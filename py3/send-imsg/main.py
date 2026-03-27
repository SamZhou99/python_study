import os
import time

# 每条消息 休息时间
SleepTimeSendMsg = 0.2
# 每隔多少条 消息休息
SleepTimeStepNum = 3
# 每隔多少条 消息休息时间
SleepTime = 2


# 发送消息
def sendMessage(index, phone_num, message_str):
    if index % SleepTimeStepNum == 0:
        time.sleep(SleepTime)
    print("{} {} {}".format(index, phone_num, message_str))
    os.system("osascript ./send-msg.scpt {} '{}'".format(phone_num, message_str))


# 读取消息
def readMessage(file_path):
    f = open(file_path, "r", encoding="utf-8")
    return f.read()


# 读取电话号码
def getPhones(file_path):
    f = open(file_path)
    return f.read().split("\n")


# 初始化
def init():
    message_str = readMessage("./message_2.txt")
    phones = getPhones("./phones_2.txt")
    index = 0
    for phone_num in phones:
        index += 1
        sendMessage(index, phone_num, message_str)
        time.sleep(SleepTimeSendMsg)


if __name__ == "__main__":
    init()
