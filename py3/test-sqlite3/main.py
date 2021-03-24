import sqlite3
import random
import math

import time


# 格式化日期时间
def getTime():
    t = time.localtime()
    return "{}-{}-{} {}:{}:{}".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)


# 范围随机数
def rand(min, max):
    return random.randint(min, max)


# 添加数据
def add(user_id, user_status_id, sales_number):
    sql = """INSERT INTO sales_order("user_id", "user_status_id", "sales_number", "create_time", "update_time") VALUES ({}, {}, {}, '{}', '{}');""".format(
        user_id, user_status_id, sales_number, getTime(), getTime())
    conn.cursor().execute(sql)
    print(sql)


# 添加测试数据
def add_test():
    for _ in range(3):
        user_status_id = rand(1, 3)
        add(1, user_status_id, 1)


# 数据库 数据 以 字典方式显示
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# 链接数据库
conn = sqlite3.connect("test.db")
conn.row_factory = dict_factory
print("sqlite open")

# add_test()

# 先把状态查询出来 存入字典 之后好以KEY取出 对应到状态📌
states_list = conn.cursor().execute("""SELECT * FROM user_states""")
d = {}
for states_item in states_list:
    d[states_item['id']] = states_item

# 查询用户列表
user_list = conn.cursor().execute("""SELECT user_info.*,user_categorys.name AS category_name FROM user_info LEFT JOIN user_categorys ON user_info.category_id=user_categorys.id""")
for user_item in user_list:
    # 将 用户信息 加入一个空 分数列表score_list
    user_item['score_list'] = []
    # 查询 该用户所有订单信息 并 将同状态的单数 相加 得到 sales_number
    sql = """SELECT id, user_status_id, SUM(sales_number) AS sales_number FROM sales_order WHERE user_id={} GROUP BY user_status_id""".format(user_item['id'])
    user_sales_order = conn.cursor().execute(sql)
    for order_item in user_sales_order:
        # 用户状态 与 状态表 数据对应📌
        temp = d[order_item['user_status_id']]
        score_list = order_item.copy()
        score_list.update(temp)
        # 计算分数 小计
        score_list['subtotal'] = score_list['score'] * score_list['sales_number']
        user_item['score_list'].append(score_list)
    print(user_item)

conn.commit()
conn.close()
