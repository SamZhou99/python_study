import random
import time


def input_number():
    while True:
        n = input('请输入一个整数：')
        try:
            n = int(n)
            break
        except ValueError:
            continue
    return n


def bot_input_number(start, end, result_tup, in_num):
    if len(result_tup) <= 0:
        return int((end-start)*0.5)
    if result_tup[0] > 0:
        return int((in_num-start)*0.5+start)
    if result_tup[0] < 0:
        return int((end-in_num)*0.5+in_num)
    return in_num


def cmp_num(n1, n2):
    if n1 > n2:
        return (-1, '??? 比 '+str(n2)+' 大')
    if n1 < n2:
        return (1, '??? 比 '+str(n2)+' 小')
    return (0, '??? 一样 '+str(n2)+' 大')


def init():
    print('猜数游戏 100-999 之间的数')
    start_num = 1000
    end_num = 9999
    result_tuple = ()
    r = random.randint(start_num, end_num)
    # print('随机数：{}'.format(r))
    in_num = 0
    count = 0
    while True:
        count += 1
        # in_num = input_number()
        in_num = bot_input_number(start_num, end_num, result_tuple, in_num)
        print("输入的数：{}".format(in_num))
        result_tuple = cmp_num(r, in_num)
        print("{}次, 结果：{}".format(count, result_tuple))
        if result_tuple[0] == 0:
            print('答案正确')
            break
        if result_tuple[0] == 1:
            end_num = in_num
        else:
            start_num = in_num
        time.sleep(0.1)


init()
