def aa(num, n):
    if num <= 0:
        print('结果n', n)
        return
    print(num, n)
    aa(num-1, n+n)


# 递归
aa(300, 1)
