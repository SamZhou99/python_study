#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
import MySQLdb
import MySQLdb.cursors
import datetime

HOST = "172.21.0.3"
# HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASS = "root"
DBNAME1 = "test1"
DBNAME2 = "test2"


# 打开数据库连接
db_test1 = MySQLdb.connect(HOST, USER, PASS, DBNAME1, PORT, charset='utf8')

db_test2 = MySQLdb.connect(HOST, USER, PASS, DBNAME2, PORT, charset='utf8')


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


def getAdministratorData():
    execute(db_test2, "TRUNCATE TABLE `administrator`")

    sql = "SELECT * FROM `administrator` ORDER BY `id`"
    result = select(db_test1, sql)
    list = []
    for rs in result:
        list.append((rs[0], rs[1], rs[2], rs[3], rs[4], rs[5],
                     rs[6], rs[7], rs[8], rs[12], rs[9]))

    try:
        executemany(db_test2, '''
            INSERT INTO `administrator` 
            (`id`,`account`,`name`,`description`,`password`,`private_key`,`remember_token`,`is_2fa`,`is_agent`,`status`,`last_login`) 
            VALUE
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''', list)
    except Exception as e:
        raise e

    return True


def getPermissionRoleData():
    execute(db_test2, "TRUNCATE TABLE `permission_role`")

    sql = "SELECT * FROM `permission_role` ORDER BY `permission_id`"
    result = select(db_test1, sql)
    list = []
    for rs in result:
        list.append((rs[0], rs[1]))

    try:
        executemany(
            db_test2, '''INSERT INTO `permission_role` (`permission_id`,`role_id`) VALUE(%s,%s)''', list)
    except Exception as e:
        raise e

    return True


def getPermissionsData():
    execute(db_test2, "TRUNCATE TABLE `permissions`")

    sql = "SELECT * FROM `permissions` ORDER BY `id`"
    result = select(db_test1, sql)
    list = []
    for rs in result:
        list.append((rs[0], rs[1], rs[2], rs[3], rs[6], rs[7]))

    try:
        executemany(
            db_test2, '''INSERT INTO `permissions` (`id`,`name`,`display_name`,`description`,`group`,`category`) VALUE(%s,%s,%s,%s,%s,%s)''', list)
    except Exception as e:
        raise e

    return True


def getRoleUserData():
    execute(db_test2, "TRUNCATE TABLE `role_user`")

    sql = "SELECT * FROM `role_user` ORDER BY `role_id`"
    result = select(db_test1, sql)
    list = []
    for rs in result:
        list.append((rs[0], rs[1]))

    try:
        executemany(
            db_test2, '''INSERT INTO `role_user` (`user_id`,`role_id`) VALUE(%s,%s)''', list)
    except Exception as e:
        raise e

    return True


def getRolesData():
    execute(db_test2, "TRUNCATE TABLE `roles`")

    sql = "SELECT * FROM `roles` ORDER BY `id`"
    result = select(db_test1, sql)
    list = []
    for rs in result:
        list.append((rs[0], rs[1], rs[2], rs[3], rs[4],
                     rs[5], rs[6], rs[9], rs[10]))

    try:
        executemany(db_test2, '''INSERT INTO `roles` (`id`,`name`,`display_name`,`description`,`left`,`right`,`depth`,`level`,`group`) VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', list)
    except Exception as e:
        raise e

    return True


def test_connect():
    rs1 = select(db_test1, "SELECT * FROM administrator LIMIT 1")
    print(rs1)
    rs2 = select(db_test2, "SELECT * FROM administrator LIMIT 1")
    print(rs2)


# test_connect()
getAdministratorData()
getPermissionRoleData()
getPermissionsData()
getRoleUserData()
getRolesData()

# 关闭数据库连接
db_test1.close()
db_test2.close()
