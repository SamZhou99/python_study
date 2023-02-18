import os

LOCAL_DIR = 'D:/Download/新建文件夹/'
LOCAL_TARGET_DIR = 'D:/Download/images/'


def getTitle(fileName):
    n = fileName.rfind('_')
    if(n == -1):
        return '?'
    return fileName[0:n]


def checkFileType(filename):
    t = ['.jfif', '.jpg', '.jpeg', '.png', '.gif']
    for n in t:
        if(filename.find(n) != -1):
            return True
    return False


def delSingFile(a):
    if len(a) <= 0:
        return []
    tempStr = a[0]
    tempTitle = getTitle(tempStr)
    tempArr = []
    arr = []
    for item in a:
        if(item.find(tempTitle) != -1):
            tempArr.append(item)
        else:
            if(len(tempArr) > 1):
                # arr.extend(tempArr)
                arr.append(tempArr)
            tempTitle = getTitle(item)
            tempArr = []
            tempArr.append(item)
    if(len(tempArr) <= 1):
        del tempArr[0]
    else:
        # arr.extend(tempArr)
        arr.append(tempArr)
    return arr


def getFileList(isTest=False):
    if(isTest):
        return ['30岁了又怎样？[17P]_1.jfif', '30岁了又怎样？[17P]_2.jfif', '30岁了又怎样？[17P]_3.jfif',
                'f-雨辰fgdf_1.jfif',
                's-雨辰fgdf_10.jfif',
                'SZ坪山高级会所小姐姐真带劲[18P]_1.jfif', 'SZ坪山高级会所小姐姐真带劲[18P]_2.jfif',
                'abc_01.jpg',
                'def_01.jpg',
                '硬件参数.png', ]
    path = os.path.abspath(LOCAL_DIR)
    all_file = os.listdir(path)
    a = []
    for file in all_file:
        if(checkFileType(file)):
            a.append(file)
    return a


def moveFile(items):
    targetDir = LOCAL_TARGET_DIR + getTitle(items[0])
    isExists = os.path.exists(targetDir)
    if(not isExists):
        os.makedirs(targetDir)
        print('ok 移动成功', isExists, targetDir)
        for item in items:
            src = LOCAL_DIR + item
            dst = targetDir + '/' + item
            os.rename(src, dst)
        return True
    else:
        print('no 已存在', isExists, targetDir)
        return False


def removeFile(items):
    targetDir = LOCAL_TARGET_DIR + getTitle(items[0])
    isExists = os.path.exists(targetDir)
    if(isExists):
        for item in items:
            src = LOCAL_DIR + item
            os.remove(src)
        return True
    else:
        print('已存在', isExists, targetDir)
        return False


def init():
    a = getFileList()
    a = delSingFile(a)
    print(len(a), '================================================================')
    count = 0

    for item in a:
        if(moveFile(item)):
            count += 1

    if(count == 0):
        print('执行删除')
        for item in a:
            removeFile(item)

print('version 20220601.1')
init()
