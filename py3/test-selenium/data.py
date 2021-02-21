def readDataFile(filename):
    f = open(filename, "r")
    data = f.read()
    list = data.split("\n")
    return list


def writeDataFile(filename, text):
    f = open(filename, 'a')
    f.write(text)
    f.close()