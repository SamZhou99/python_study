total_count = 0


def bf(n):
    global total_count
    total_count = 0
    prime_number = []
    for i in range(2, n):
        res = is_prime(i)
        if res > 0:
            prime_number.append(res)
    return prime_number


def is_prime(x):
    global total_count
    total_count += 1
    i = 2
    while i * i <= x:
        total_count += 1
        if x % i == 0:
            return -1
        i += 1
    return x


def eratosthenes(n):
    global total_count
    total_count = 0
    prime_number = []
    isPrime = [False] * n
    i = 2
    while i < n:
        total_count += 1
        if not isPrime[i]:
            prime_number.append(i)
            j = i * i
            while j < n:
                total_count += 1
                isPrime[j] = True
                j += i
        i += 1
    return prime_number


def prime_check(n):
    global total_count
    total_count = 0
    i = 3
    prime_numbers = [2]
    while i <= n:
        if prime_check_2(i, prime_numbers):
            prime_numbers.append(i)
        i += 1
    return prime_numbers


def prime_check_2(n, prime_number):
    global total_count
    result = True
    for i in prime_number:
        total_count += 1
        if n % i == 0:
            return False
            result = False
    return result


def init():
    global total_count
    my_number = 200
    result = bf(my_number)
    result_len = len(result)
    print("要计算的数：", my_number)
    print("计算次数：", total_count)
    print("素数个数：", result_len)
    print("素数：", result)

    result = eratosthenes(my_number)
    result_len = len(result)
    print("要计算的数：", my_number)
    print("计算次数：", total_count)
    print("素数个数：", result_len)
    print("素数：", result)

    result = prime_check(my_number)
    result_len = len(result)
    print("要计算的数：", my_number)
    print("计算次数：", total_count)
    print("素数个数：", result_len)
    print("素数：", result)


init()
