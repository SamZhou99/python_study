totalCount = 0


def bf(n):
    global totalCount
    totalCount = 0
    count = 0
    for i in range(2, n):
        totalCount += 1
        if isPrime(i):
            count += 1
    return count, totalCount


def isPrime(x):
    global totalCount
    i = 2
    while i * i <= x:
        totalCount += 1
        if x % i == 0:
            return False
        i += 1
    print("素数", x)
    return True


def init():
    print(bf(10000))


if __name__ == "__main__":
    init()
