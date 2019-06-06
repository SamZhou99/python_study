from __future__ import division
import pymysql
import datetime


# HOST = "172.21.0.3"
HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASS = "root"
DBNAME1 = "yyh_central_20190605"
DBNAME2 = "yyh_central"

config1 = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'root',
    'db':'yyh_central_20190605',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
}

config2 = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'root',
    'db':'yyh_central',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
}


# 打开数据库连接
# db_test1 = pymysql.connect(HOST, USER, PASS, DBNAME1, PORT, charset='utf8')
# db_test2 = pymysql.connect(HOST, USER, PASS, DBNAME2, PORT, charset='utf8')
db_test1 = pymysql.connect(**config1)
db_test2 = pymysql.connect(**config2)


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
    sql = "SELECT * FROM `administrator` ORDER BY `id`"
    result = select(db_test1, sql)
    list = []
    for rs in result:
        list.append((rs['id'], rs['account'], rs['name'], 
        rs['description'], rs['password'], rs['position_id'], 
        rs['private_key'], rs['remember_token'], rs['is_2fa'],
        rs['is_agent'], rs['status'], rs['last_login'], 
        rs['updated_at'], rs['created_at']))
    
    execute(db_test2, "TRUNCATE TABLE `administrator`")
    try:
        executemany(db_test2, '''
            INSERT INTO `administrator` 
            (`id`,`account`,`name`,
            `description`,`password`,`position_id`,
            `private_key`,`remember_token`,`is_2fa`,
            `is_agent`,`status`,`last_login`,
            `updated_at`,`created_at`) 
            VALUE
            (%s,%s,%s,
            %s,%s,%s,
            %s,%s,%s,
            %s,%s,%s,
            %s,%s)
            ''', list)
    except Exception as e:
        raise e

    return True


def getAdminPermissionData():
    sql = "SELECT * FROM `admin_permission_relation`"
    result = select(db_test1, sql)
    list = []
    for rs in result:
        list.append((rs['permission_id'], rs['admin_id'], rs['operate']))
    
    execute(db_test2, "TRUNCATE TABLE `admin_permission_relation`")
    try:
        executemany(db_test2, '''
            INSERT INTO `admin_permission_relation` 
            (`permission_id`,`admin_id`,`operate`) 
            VALUE
            (%s,%s,%s)
            ''', list)
    except Exception as e:
        raise e

    return True


def getPermissionRoleData():
    sql = "SELECT * FROM `permission_role`"
    result = select(db_test1, sql)
    list = []
    for rs in result:
        list.append((rs['permission_id'], rs['role_id']))
    
    execute(db_test2, "TRUNCATE TABLE `permission_role`")
    try:
        executemany(db_test2, '''
            INSERT INTO `permission_role` 
            (`permission_id`,`role_id`) 
            VALUE
            (%s,%s)
            ''', list)
    except Exception as e:
        raise e

    return True


def getPermissionData():
    sql = "SELECT * FROM `permissions`"
    result = select(db_test1, sql)
    list = []
    for rs in result:
        list.append((rs['id'], rs['name'], rs['display_name'], 
        rs['description'], rs['group'], rs['category']))
    
    execute(db_test2, "TRUNCATE TABLE `permissions`")
    try:
        executemany(db_test2, '''
            INSERT INTO `permissions` 
            (`id`,`name`,`display_name`,`description`,`group`,`category`) 
            VALUE
            (%s,%s,%s,%s,%s,%s)
            ''', list)
    except Exception as e:
        raise e

    return True




def test_connect():
    rs1 = select(db_test1, "SELECT 1+1")
    rs2 = select(db_test2, "SELECT 1+1")
    return True

def close_connect():
    db_test1.close()
    db_test2.close()


def start_move_data():
    getAdministratorData()
    getAdminPermissionData()
    getPermissionRoleData()
    getPermissionData()


if test_connect():
    print('connect succeed')
    start_move_data()
    close_connect()
    print('complete...ok...!')
else:
    print('connect error')
