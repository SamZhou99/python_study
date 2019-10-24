import random

# 做多少题
max_num = 10
total = 0
right = 0
error = 0


def print_statistical():
    global total, right, error
    print('总是题数：{}，正确：{}，错误：{}'.format(total, right, error))
    print('')


def get_input_num():
    return int("".join(list(filter(str.isdigit, input("等于？")))))


for i in range(1, max_num):
    r = random.randint(0, 1)
    x = random.randint(1, 9)
    y = random.randint(1, 19)

    if r == 1:
        print('{} + {} = ?\t'.format(x, y))
    else:
        x = max(x, y)
        y = min(x, y)
        print('{} - {} = ?\t'.format(x, y))

    input_number = get_input_num()
    total += 1

    if r == 1 and x+y == input_number:
        right += 1
        print('√    👍👏👨‍✈️  你好棒！\n')
    elif r == 0 and x-y == input_number:
        right += 1
        print('√    👍👏👨‍✈️  你好棒！\n')
    else:
        error += 1
        if r == 1:
            d = x+y
        else:
            d = x-y
        print('×    👎💩😭  傻瓜! 应该等于={}\n'.format(d))
    print_statistical()
