import sqlite3
import module_plistlib
import time
from ClassSqlite import ClassSqlite

DBPath = "/Users/sam/Library/Messages/chat.db"
SQLite = ClassSqlite(DBPath)


def view_data(alldata, field):
    for item in alldata:
        # print("📊数据：：：", item[field])
        res = module_plistlib.parseImessageText(item[field])
        print("👹结果：", item["ROWID"], res)


def init():
    print("----------------- chat")
    sql = "SELECT ROWID, properties FROM chat WHERE state=3 LIMIT {};".format(10)
    res = SQLite.select(sql)
    view_data(res, "properties")

    print("----------------- message")
    sql = "SELECT ROWID, attributedBody FROM message ORDER BY ROWID DESC LIMIT {};".format(
        900
    )
    res = SQLite.select(sql)
    view_data(res, "attributedBody")

    SQLite.finish()
    print("执行完成")


init()
