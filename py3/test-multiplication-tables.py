def startMultiplication(maxNum):
    for x in range(1, maxNum+1):
        for y in range(1, x+1):
            print("%dx%d=%d" % (y, x, x*y), end='\t')
        print('')


startMultiplication(9)
