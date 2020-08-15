from __future__ import division
import datetime
import pymysql
import time

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'lajiao_video',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
mysql_conn = pymysql.connect(**config)


def close():
    mysql_conn.close()


def insert(title, age, timedate):
    sql = "INSERT INTO `test`.`content`(`title`, `age`, `timedate`) VALUES ('{0}', '{1}', '{2}')".format(
        title, age, timedate)
    print(sql)
    cursor = mysql_conn.cursor()
    cursor.execute(sql)
    cursor.close()


def select():
    sql = "SELECT * FROM articles ORDER BY id DESC LIMIT {0}".format(
        '10')
    print(sql)
    with mysql_conn.cursor() as cursor:
        cursor.execute(sql)
        result_list = cursor.fetchall()
        for item in result_list:
            print(item['id'], item['video'])


# insert('标题', 9, time.strftime('%Y-%m-%d %M:%I:%S', time.localtime()))
select()
close()
