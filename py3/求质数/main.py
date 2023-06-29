import time

start = 0
nums = []


def startTime():
    global start
    start = time.perf_counter()


def endTime():
    global start
    end = time.perf_counter()
    ms = end - start
    print("耗时：{} 毫秒".format(ms * 1000))


def to_be_divisible_by(num, i):
    n1 = int(num / i)
    return n1 * i == num


def prime_number(num):
    if num == 2 or num == 3:
        return num

    global nums
    if len(nums) > 0 and num > 10:
        for i in nums:
            if to_be_divisible_by(num, i):
                return -1
        return num

    for i in range(2, num):
        if i < num:
            if to_be_divisible_by(num, i):
                return -1
    return num


def init(max_num):
    global nums
    for i in range(2, max_num + 1):
        num = prime_number(i)
        if num > 0:
            nums.append(num)
    print(len(nums))
    print(nums[len(nums) - 10 :])


startTime()

# # 4
# init(10)

# # 8个
# init(20)

# # 25
# init(100)

# # 168个
# init(1000)


# # 1229个
# init(10000)

# # 9592个
# init(100000)

print(prime_number(99991))

endTime()
