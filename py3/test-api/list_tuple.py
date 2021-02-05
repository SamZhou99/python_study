# 列表
list = ['a', 'b', 'c', 'd', 4, 5, 6, 7, 7]
numbers = [2, 8, 4, 9, 0, 5, 6]

# list[索引开始:索引结束:索引步长]
print(list[0::2])

# 最大 最小 长度
print(min(numbers))
print(max(numbers))
print(len(numbers))

# 链接列表(或list = list + list)
new_list = [8, 9, 10]
list.extend(new_list)
print(list)

# 删除
del list[0]
print(list)

# 替换
list[1:4] = [0]
print(list)

# 插入
list.insert(int(len(list) / 2), 99)
print(list)

# 移除 list.pop(索引) (默认删除最后一个)
list.pop()
print(list)

# 相反
list.reverse()
print(list)

# 排序
numbers.sort()
print(numbers)

# 统计出现的次数
print(list.count(7))

# 查找 如果找不到内容就会报错
try:
    print(list.index(70))
except Exception as identifier:
    print('异常：列表中 没有找到 相应的数据')

# 乘法口诀
for m1 in range(1, 10):
    for m2 in range(1, m1 + 1):
        print("{}x{}={}".format(m2, m1, m1 * m2), end='\t')
    print()
