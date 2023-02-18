from __future__ import division
import datetime
import random
import pymysql
import time


config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'test',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
mysql_conn = pymysql.connect(**config)


def close():
    mysql_conn.close()


def insert(key, value):
    sql = "INSERT INTO `list`(`key`, `value`) VALUES ('{0}', '{1}')".format(
        key, value)
    # print(sql)
    cursor = mysql_conn.cursor()
    cursor.execute(sql)
    cursor.close()


def select():
    sql = "SELECT * FROM list ORDER BY id DESC LIMIT {0}".format('10')
    print(sql)
    with mysql_conn.cursor() as cursor:
        cursor.execute(sql)
        result_list = cursor.fetchall()
        for item in result_list:
            print(item['id'])


for i in range(1, 10000):
    r = random.randint(1000, 9999)
    insert('key_'+str(r), 'vlaue_'+str(r))
# select()
# close()
print("结束")
