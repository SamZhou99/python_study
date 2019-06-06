from __future__ import division
import pymysql
import datetime


# HOST = "172.21.0.3"
HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASS = "root"
DBNAME1 = "yyh_central"

config1 = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'yyh_central_20190605',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}


# 打开数据库连接
# db_test1 = pymysql.connect(HOST, USER, PASS, DBNAME1, PORT, charset='utf8')
# db_test2 = pymysql.connect(HOST, USER, PASS, DBNAME2, PORT, charset='utf8')
db_test1 = pymysql.connect(**config1)


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


def Permissions():
    sql = "SELECT * FROM `permissions` ORDER BY `id`"
    result = select(db_test1, sql)
    list = []
#     `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `name` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `display_name` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
#   `description` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
#   `created_at` timestamp NULL DEFAULT NULL,
#   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
#   `group` char(64) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
#   `category` enum('PAGE','API','ACTION','REPORT_COLUMN','REPORT_SCOPE','') COLLATE utf8mb4_unicode_ci DEFAULT NULL,

    list.append(('', 'page-game-type', '游戏平台分类',
                 '游戏平台分类', 'casino-game', 'PAGE'))

    execute(db_test1, "TRUNCATE TABLE `permissions`")
    try:
        executemany(db_test1, '''
            INSERT INTO `permissions` 
            (`id`,`name`,`display_name`,
            `description`,`group`,`category`,,
            `updated_at`,`created_at`) 
            VALUE
            (%s,%s,%s,
            %s,%s,%s,
            %s,%s)
            ''', list)
    except Exception as e:
        raise e

    return True


def test_connect():
    rs1 = select(db_test1, "SELECT 1+1")
    return True


def close_connect():
    db_test1.close()


def start_move_data():
    Permissions()


if test_connect():
    print('connect succeed')
    start_move_data()
    close_connect()
    print('complete...ok...!')
else:
    print('connect error')
