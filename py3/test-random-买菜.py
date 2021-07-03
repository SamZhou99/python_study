# 共有10人，每天安排3人买菜，随机平均减少重复安排
import random

DAY = 10
COUNT = 3

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(a)

for i in range(DAY):
    print('星期{}'.format(i % 7+1), end='\t')
    for num in range(COUNT):
        maicai = a.pop(0)
        a.append(maicai)
        print(maicai, end=',')
    print()
