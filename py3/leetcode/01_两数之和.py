import time

# nums = [2, 7, 11, 15]
# target = 9

# nums = [3, 2, 4]
# target = 5

nums = [3, 3]
target = 6

start = 0
end = 0
sum = 0


def startTime():
    global start
    start = time.time()


def endTime():
    global end, sum
    end = time.time()
    sum = end-start
    print('运行时长：', sum)


def twoSum(nums, target):
    i = 0
    for n in nums:
        n2 = nums.index(target-n, i+1)
        if n2:
            return print(i, n2)
        i = +1


startTime()
twoSum(nums, target)
endTime()
