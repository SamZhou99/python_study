COUNT = 50
for i in range(COUNT):
    i = i + 1
    if i < 10:
        i = "00" + str(i)
    elif i < 100:
        i = "0" + str(i)
    email_str = "guest{}|guest{}@coinbtc.us|aA123456|5|GB".format(i, i)
    print(email_str)
