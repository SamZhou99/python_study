from __future__ import division
import pymysql
import random

db = pymysql.connect(host='127.0.0.1', user='root',
                     password='root', db='test', port=3306)

# CREATE TABLE `test` (
#   `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `cost_d` double(12,4) unsigned zerofill DEFAULT 0000000.0000,
#   `cost_f` float(12,4) unsigned zerofill DEFAULT 0000000.0000,
#   `cost_dd` decimal(12,4) unsigned zerofill DEFAULT 00000000.0000,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=latin1;


def truncate():
    sql = 'TRUNCATE TABLE test'
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    print('truncate ok')


def insert(d, f, dd):
    cursor = db.cursor()
    num_d = d
    num_f = f
    num_dd = dd
    sql = "INSERT INTO test(cost_d, cost_f, cost_dd) VALUE(" + \
        str(num_d)+", "+str(num_f)+", "+str(num_dd)+")"
    print('insert ok', sql)
    cursor.execute(sql)
    db.commit()


def insertBatch(total=20):
    for i in range(total):
        i += 1
        d = float(i*99 / random.random())
        f = float(i*99 / random.random())
        dd = float(i*99 / random.random())
        insert(d, f, dd)
        print(d, f, dd)


def query():
    cursor = db.cursor()
    sql = 'SELECT * FROM test'
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(getNumFormat(row[1]), getNumFormat(row[2]), getNumFormat(row[3]))


def getNumFormat(num):
    return "{:.4f}".format(num)


truncate()
insertBatch(1000)
query()
db.close()
