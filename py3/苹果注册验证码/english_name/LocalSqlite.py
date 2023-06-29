import sqlite3
import time
from config.db import DB_Config


class LocalSqlite:
    def __init__(self) -> None:
        config = DB_Config()
        self.conn = sqlite3.connect(config.sqlite_english_name)
        self.conn.row_factory = dict_factory
        self.Test()

    def Test(self):
        list = self.Query("""SELECT * FROM name_list LIMIT 1""")
        for item in list:
            print(item)

    def InitTabel(self):
        pass

    def ResetTable(self):
        self.UpdateAllStatus(1)

    def Query(self, sql):
        result = self.conn.cursor().execute(sql)
        self.conn.commit()
        return result

    def Insert(self, status, word, type):
        sql = """INSERT INTO name_list(`status`, `word`, `type`) VALUES({},"{}","{}")""".format(
            status, word, type
        )
        return self.Query(sql)

    def Delete(self, id):
        sql = """DELETE FROM name_list WHERE id={}""".format(id)
        return self.Query(sql)

    def Update(self, id, status):
        sql = """UPDATE name_list SET `status`={} WHERE id={}""".format(status, id)
        return self.Query(sql)

    def UpdateAllStatus(self, status=1):
        sql = """UPDATE name_list SET `status`={}""".format(status)
        return self.Query(sql)

    def List(self, limit=1) -> list:
        sql = """SELECT * FROM name_list ORDER BY id DESC LIMIT {}""".format(limit)
        return self.Query(sql)

    def Count(self):
        sql = """SELECT COUNT(*) AS total FROM name_list WHERE status=1"""
        return self.Query(sql)

    def Find(self, id) -> list:
        sql = """SELECT * FROM name_list WHERE id={} LIMIT 1""".format(id)
        return self.Query(sql)

    def FindWord(self, word) -> list:
        sql = """SELECT * FROM name_list WHERE word="{}" LIMIT 1""".format(word)
        return self.Query(sql)

    def FindRandom(self):
        sql = """SELECT * FROM name_list WHERE status=1 GROUP BY id ORDER BY RANDOM() LIMIT 1"""
        return self.Query(sql)

    def FindRandomLastName(self):
        sql = """SELECT * FROM name_list WHERE status=1 AND type='last_name' GROUP BY id ORDER BY RANDOM() LIMIT 1"""
        return self.Query(sql)

    def Close(self):
        self.conn.close()


# 格式化日期时间
def getTime():
    t = time.localtime()
    return "{}-{}-{} {}:{}:{}".format(
        t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec
    )


# 数据库 数据 以 字典方式显示
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
