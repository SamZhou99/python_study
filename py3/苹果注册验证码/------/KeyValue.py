import time


def localTime():
    return time.strftime("%Y-%m-%d %M:%I:%S", time.localtime())


arr = []
for i in range(3):
    dic = {
        "id": i,
        "ip": "127.0.0.1:80",
        "status": "0",
        "create_datetime": localTime(),
        "update_datetime": localTime(),
    }
    arr.append(dic)

keys = []
values = []
for item in arr:
    for i in item.items():
        key = i[0]
        value = i[1]
        if key not in keys:
            keys.append("`{}`".format(key))
        values.append("`{}`".format(value))
print(keys, values)
