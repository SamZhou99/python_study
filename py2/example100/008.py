#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 九九乘法表

for i in range(1, 10):
    print ""
    for j in range(1, i+1):
        print "%d*%d=%d\t" % (j, i, i*j),
print "over"
