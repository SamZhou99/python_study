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
        # return (-1, '??? 比 '+str(n2)+' 大')
        return (-1, '您输入的数字太小了')
    if n1 < n2:
        # return (1, '??? 比 '+str(n2)+' 小')
        return (1, '您输入的数字太大了')
    return (0, '这个数与 '+str(n2)+' 一样大')


def init():
    print('\n猜数游戏：这个数在 1000-9999 之间')
    time.sleep(1)

    start_num = 1000
    end_num = 9999
    result_tuple = ()
    r = random.randint(start_num, end_num)
    # print('这个随机数是：{}'.format(r))

    print("""
请输入 1 或者 2 确认游玩方式。
1: 人工输入游玩
2: 电脑输入游玩
    """)
    in_type_num = input_number()

    in_num = 0
    count = 0
    while True:
        count += 1
        if in_type_num == 1:
            in_num = input_number()
        else:
            in_num = bot_input_number(start_num, end_num, result_tuple, in_num)
        print("\n输入的数：{}".format(in_num))

        result_tuple = cmp_num(r, in_num)
        print("{}次, 比对结果：{}".format(count, result_tuple))

        if result_tuple[0] == 0:
            print('\n答案正确，游戏结束。')
            time.sleep(2)
            break
        if result_tuple[0] == 1:
            end_num = in_num
        else:
            start_num = in_num
        time.sleep(0.1)


init()
