import random

max_num = 10
total = 0
right = 0
error = 0


def print_statistical():
    global total, right, error
    print('总是题数：{}，正确：{}，错误：{}'.format(total, right, error))
    print('')


for x in range(1, max_num):
    for y in range(x, max_num):
        i = random.randint(5, 19)
        j = random.randint(1, 19)
        print('{} + {} = ?\t'.format(i, j))
        input_number = int("".join(list(filter(str.isdigit, input("等于？")))))
        total += 1
        if i+j == input_number:
            right += 1
            print('√    👍\n')
        else:
            error += 1
            print('×    👎\n')
        print_statistical()
