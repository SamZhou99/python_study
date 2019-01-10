#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：斐波那契数列。


# 方法一 使用for循环
def fib1(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


# 方法二 使用递归
def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n-1)+fib2(n-2)


# 方法三 使用 for range
def fib3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs



count = 35


print fib3(count)
print fib1(count)
print fib2(count)

