#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import datetime

HOST = "172.21.0.4"
USER = "root"
PASS = "root"
DBNAME = "jimo100"


# 打开数据库连接
db = MySQLdb.connect(HOST, USER, PASS,
					 DBNAME, charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()
dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
	cursor.execute("INSERT INTO test_tables (title, content, created_at, updated_at) VALUES (%s, %s, %s, %s)", ('标题', '内容', dt, dt))
except Exception as e:
	raise e

try:
	cursor.execute("SELECT * FROM test_tables ORDER BY id DESC LIMIT 5")
	results = cursor.fetchall()
	for row in results:
		print row[0], row[1], row[3]
	# 提交到数据库执行
	db.commit()
except Exception as e:
	raise e
	# 发生错误时回滚
	db.rollback()
	print "Error: unable to fecth data"


# 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()

# print "Database version : %s " % data

# 关闭数据库连接
db.close()

