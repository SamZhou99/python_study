#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
import pymysql
import datetime
import requests
import re


config1 = {
	# 'host': '127.0.0.1',
	'host': '172.21.0.3',
	'port': 3306,
	'user': 'root',
	'password': 'root',
	'db': 'test_python',
	'charset': 'utf8mb4',
	'cursorclass': pymysql.cursors.DictCursor,
}


# 打开数据库连接
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


def query(db, sql, data=None):
	cursor = db.cursor()
	cursor.execute(sql, data)
	return cursor.fetchall()


def get_html_gb2312(url):
	html = requests.get(url)
	return html.content


def get_html_utf8(url):
	html = requests.get(url)
	return html.content


def get_html_paragraph(str, start, end):
	n1 = str.index(start)+len(start)
	n2 = str.index(end, n1)
	return str[n1:n2]


def analyze_html(url):
	html = get_html_utf8(url)
	# html = get_html_gb2312(url)
	print html
	temp = re.findall(r"<a.*?href=\"http.*?<\/a>", html, re.I)
	for item in temp:
		link = get_html_paragraph(item, 'href="', '"')
		name = get_html_paragraph(item, '>', '<')
		name = name.strip()
		if name:
			print '【'+name+'】', link

# url = 'https://av02.net/?ulc_safe_link=551'
# url = 'http://www.daroubang.info'
url = 'https://fulione03.com/'
analyze_html(url)
