import pymysql
import time

mysql_conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    db='test'
)


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
    sql = "SELECT * FROM content ORDER BY id DESC LIMIT {0}".format(
        '10')
    print(sql)
    with mysql_conn.cursor() as cursor:
        cursor.execute(sql)
        result_list = cursor.fetchall()
        for result_one in result_list:
            print(result_one)


insert('标题', 9, time.strftime('%Y-%m-%d %M:%I:%S', time.localtime()))
select()
close()
