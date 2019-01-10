#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
import time
from sys import stdout
from math import sqrt

temp=0

def primeNumber(num):
	k = int(sqrt(num + 1))
	for i in range(2, k + 1):
		if num % i == 0:
			global temp
			temp = max(temp, i)
			print num, i, temp
			return False
			break
	return num
	


for x in xrange(100000, 200000):
	p = primeNumber(x)
	if p:
		print '素数：', p
	time.sleep(0.1)
