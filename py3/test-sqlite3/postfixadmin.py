import sqlite3


# 数据库 数据 以 字典方式显示
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# 链接数据库
conn = sqlite3.connect("postfixadmin.db")
conn.row_factory = dict_factory
print("sqlite open")

# 先把状态查询出来 存入字典 之后好以KEY取出 对应到状态📌
states_list = conn.cursor().execute(
    """SELECT * from sqlite_master WHERE type='table' """
)
d = {}
for states_item in states_list:
    # d[states_item["id"]] = states_item
    print(states_item)

conn.commit()
conn.close()
