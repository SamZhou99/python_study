from __future__ import division
import pymysql
import datetime

# HOST = "172.21.0.3"
HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASS = "root"
DBNAME1 = "yyh_central_old"
DBNAME2 = "yyh_central"


# 打开数据库连接
db_test1 = pymysql.connect(HOST, USER, PASS, DBNAME1, PORT, charset='utf8')

db_test2 = pymysql.connect(HOST, USER, PASS, DBNAME2, PORT, charset='utf8')


def execute(db, sql, data=None):
    try:
        cursor = db.cursor()
        cursor.execute(sql, data)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return True


def executemany(db, sql, data):
    try:
        cursor = db.cursor()
        cursor.executemany(sql, data)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return True


def select(db, sql, data=None):
    cursor = db.cursor()
    cursor.execute(sql, data)
    return cursor.fetchall()


def getNumFormat(num):
    return "{:.4f}".format(num)








def clearData():
    execute(db_test2, "TRUNCATE TABLE `tm_task`")
    execute(db_test2, "TRUNCATE TABLE `tm_task_telephone`")
    execute(db_test2, "TRUNCATE TABLE `tm_telephone`")
    execute(db_test2, "TRUNCATE TABLE `tm_telephone_admin_relation`")
    execute(db_test2, "TRUNCATE TABLE `tm_telephone_other_info`")
    execute(db_test2, "TRUNCATE TABLE `tm_telephone_upload_log`")
    execute(db_test2, "TRUNCATE TABLE `tm_voip_log`")
    execute(db_test2, "TRUNCATE TABLE `tm_voip_log_inspection`")
    execute(db_test2, "TRUNCATE TABLE `tm_voip_log_tm_task_relation`")







def test_connect():
    rs1 = select(db_test1, "SELECT * FROM administrator LIMIT 1")
    # print(rs1)
    rs2 = select(db_test2, "SELECT * FROM administrator LIMIT 1")
    # print(rs2)
    return True


if test_connect():
    clearData()    
    # 关闭数据库连接
    db_test1.close()
    db_test2.close()
