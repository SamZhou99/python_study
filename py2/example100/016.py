#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

if __name__ == '__main__':

	# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
	print(datetime.date.today().strftime('%Y/%m/%d'))

	# 创建日期对象
	miyazakiBirthDate = datetime.date(1941, 1, 5)

	print(miyazakiBirthDate.strftime('%Y/%m/%d'))

	# 日期算术运算
	miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)

	print(miyazakiBirthNextDay.strftime('%Y/%m/%d'))

	# 日期替换
	miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

	print(miyazakiFirstBirthday.strftime('%Y/%m/%d'))
