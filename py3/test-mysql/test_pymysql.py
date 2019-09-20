import pymysql

mysql_conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    db='jimo100'
)


def close():
    mysql_conn.close()


def select():
    sql = "SELECT a_id,a_title FROM articles ORDER BY a_id DESC LIMIT {0}".format('10')
    print(sql)
    with mysql_conn.cursor() as cursor:
        cursor.execute(sql)
        result_list = cursor.fetchall()
        for result_one in result_list:
            print(result_one)


select()
close()
