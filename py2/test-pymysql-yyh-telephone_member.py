#!/usr/bin/env python
# coding=utf-8

from __future__ import division
import pymysql
import datetime
import math
import time
import requests
import AES_ECB

# HOST = "172.21.0.3"
HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASS = "root"
DBNAME1 = "yyh_central_telephone_member"
DBNAME2 = "yyh_central"



pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]


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
    return "{:.2f}".format(num)


def getTelephoneMember(pageIndex, pageLimit):
    # total 47556
    sql = "SELECT t.phone,tm.member_id FROM telephone AS t JOIN telephone_member AS tm ON tm.telephone_id=t.id LIMIT " + \
        str(pageIndex) + "," + str(pageLimit)
    result = select(db_test1, sql)
    list = []
    for rs in result:
        phone = AES_ECB.decryptAES(rs[0])
        d = (rs[0], phone, rs[1])
        list.append(d)
        # print(d)
    return list


def saveTelephoneMember(listData):
    try:
        executemany(
            db_test1, '''INSERT INTO `phone_member` (`phone`,`telephone`,`member_id`) VALUE(%s,%s,%s)''', listData)
    except Exception as e:
        raise e
    return True


def getPhoneMember(pageIndex, pageLimit):
    # total 47556
    sql = "SELECT * FROM phone_member LIMIT " + \
        str(pageIndex) + "," + str(pageLimit)
    result = select(db_test1, sql)
    s = ''
    for rs in result:
        s += str(rs[3]) + '_' + str(rs[2]) + ','
    # print(rs)
    return s


def dbClose():
    # 关闭数据库连接
    db_test1.close()
    db_test2.close()


def test_connect():
    rs1 = select(db_test1, "SELECT * FROM administrator LIMIT 1")
    # print(rs1)
    rs2 = select(db_test2, "SELECT * FROM administrator LIMIT 1")
    # print(rs2)


def test_import():
    execute(db_test1, "TRUNCATE TABLE `phone_member`")
    total = 47556
    pageIndex = 0
    pageLimit = 100
    pageTotal = int(math.ceil(total / pageLimit))
    for x in range(pageTotal):
        listData = getTelephoneMember(pageIndex, pageLimit)
        print(pageIndex, total, getNumFormat(pageIndex / total * 100) + '%')
        saveTelephoneMember(listData)
        pageIndex += pageLimit
        time.sleep(0.05)


def test_export():
    total = 47556
    pageIndex = 0
    pageLimit = 100
    pageTotal = int(math.ceil(total / pageLimit))

    for x in range(pageTotal):
        strData = getPhoneMember(pageIndex, pageLimit)
        time.sleep(0.05)

        test_request(strData)
        time.sleep(0.2)

        print(pageIndex, total, getNumFormat(pageIndex / total * 100) + '%')
        pageIndex += pageLimit


def test_request(strData):
    myData = {'data': strData}
    url = 'http://ininder.laravel.admin/api/import-member-tel'
    r = requests.post(url, data=myData)
    if r.status_code == requests.codes.ok:
        print('==========================================================')
        print(r.text)
        return True
    print('Abnormity：', r.status_code)


test_connect()


# test_import()
test_export()


dbClose()
