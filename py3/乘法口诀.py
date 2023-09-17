max_num = 9
for i in range(1, max_num+1):
    print()
    for j in range(1, i+1):
        print("{}x{}={} ".format(i, j,  i * j), end="")
