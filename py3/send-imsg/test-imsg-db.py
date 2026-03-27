import sqlite3
import module_plistlib


def view_data(alldata):
    for item in alldata:
        res, err = module_plistlib.decodedPlist(item[0])
        if err:
            print("Error:", err)
        else:
            print(res)


def init():
    # 连接到SQLite数据库
    db_path = "/Users/sam/Library/Messages/chat.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # 查询BLOB数据
    cursor.execute(
        "SELECT properties FROM chat WHERE state=3 LIMIT ?;",
        (10,),
    )
    # blob_data = cursor.fetchone()[0]
    view_data(cursor)
    # 关闭连接
    conn.close()
    print("执行完成")


init()
