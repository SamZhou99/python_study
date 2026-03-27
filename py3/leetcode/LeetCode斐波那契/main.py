import time

start_num = 0
end_num = 0
sum_num = 0


def start_time():
    global start_num
    start_num = time.time()


def end_time():
    global end_num, sum_num
    end_num = time.time()
    sum_num = end_num / 1000 - start_num / 1000
    # return sum_num
    return "耗时: {:.6f}秒".format(end_num - start_num)


def calculate(num):
    if num <= 1:
        return num
    return calculate(num - 1) + calculate(num - 2)


def recurse(num):
    pass


def iterate(num):
    if num <= 1:
        return num
    n1 = 0
    n2 = 1
    for i in range(1, num):
        n3 = n1 + n2
        n1, n2 = n2, n3
    return n3


def init():
    num = 35

    start_time()
    result = iterate(num)
    print(end_time(), result)

    start_time()
    result = calculate(num)
    print(end_time(), result)


init()
