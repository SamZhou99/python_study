from __future__ import division
import pymysql


db_test = pymysql.connect(host='127.0.0.1', user='root',
                          password='root', db='test', port=3306)

db_yyh = pymysql.connect(host='127.0.0.1', user='root',
                         password='root', db='yyh_central', port=3306)


def execute(db, sql):
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    return True


def truncate(db, table):
    execute(db, 'TRUNCATE TABLE '+table)
    return True


def select(db, sql):
    cursor = db.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def getNumFormat(num):
    return "{:.4f}".format(num)


def getAdminData():
    sql = "SELECT * FROM `administrator` LIMIT 0, 1000"
    result = select(db_test, sql)
    truncate(db_yyh, "administrator")
    for rs in result:
        print(rs)
        execute(db_yyh, "INSERT INTO administrator () VALUE()")


getAdminData()
