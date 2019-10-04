maxNum = 10
for x in range(1, maxNum):
    for y in range(x, maxNum):
        print('{} + {} = ?\t'.format(x, y))
        xx = int( input("等于几？") )
        if x+y == xx:
            print('√    正确\n')
        else:
            print('×    错误\n')
    print('')
