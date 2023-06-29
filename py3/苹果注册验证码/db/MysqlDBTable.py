import time
from db.MysqlDB import MysqlDB


def localTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def insertKeysValues(arr):
    keys = []
    values = []
    for item in arr:
        v = []
        for i in item.items():
            key = "`{}`".format(i[0])
            value = "'{}'".format(i[1])
            if key not in keys:
                keys.append("{}".format(key))
            v.append("{}".format(value))
        values.append("(" + ",".join(v) + ")")
    return ",".join(keys), ",".join(values)


def updateKeyValues(dic):
    arr = []
    for k in dic:
        key = "`{}`".format(k)
        value = "'{}'".format(dic[k])
        setValue = "{}={}".format(key, value)
        arr.append(setValue)
    return ",".join(arr)


class MysqlDBTable(MysqlDB):
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def __init__(self, table) -> None:
        self.table = table
        self.db = MysqlDB()

    def Close(self):
        self.db.Close()
        self.db = None
        return True

    def Add(self, fieldArrDic):
        keys, values = insertKeysValues(fieldArrDic)
        sql = "INSERT INTO `{}`({}) VALUES {}".format(self.table, keys, values)
        return self.db.Query(sql)

    def Delete(self, id):
        sql = "DELETE FROM `{}` WHERE id={}".format(self.table, id)
        return self.db.Query(sql)

    def Update(self, id, fieldDic):
        sql = "UPDATE `{}` SET {} WHERE id={}".format(
            self.table, updateKeyValues(fieldDic), id
        )
        return self.db.Query(sql)

    def Select(self, where):
        sql = "SELECT * FROM {} {}".format(self.table, where)
        return self.db.Select(sql)
