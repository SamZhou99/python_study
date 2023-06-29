def arithmetic_progression(start_num, step_num, end_num):
    n1 = end_num - start_num
    n2 = n1 / step_num
    n3 = n2 + 1
    return int(n3)


def sum_continuous_numbers(start_num, end_num):
    n1 = start_num + end_num
    n2 = end_num - start_num + 1
    n3 = n1 * n2 * 0.5
    return int(n3)


result = arithmetic_progression(12, 3, 999)
print(result)


result = sum_continuous_numbers(1, 1000)
print(result)
