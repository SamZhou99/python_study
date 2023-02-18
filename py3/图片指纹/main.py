from PIL import Image
import imagehash
import os
import time


def get_img_hash(img_path):
    return imagehash.dhash(Image.open(img_path), 9)


def check_file_type(filename):
    t = ['.jfif', '.jpg', '.jpeg', '.png', '.gif']
    for n in t:
        if(filename.find(n) != -1):
            return True
    return False


def get_file_list(path):
    if(os.path.exists(path)):
        return os.listdir(os.path.abspath(path))
    return []


def campHash(hash1, hash2):
    n = 0
    # hash长度不同返回-1,此时不能比较
    if len(hash1) != len(hash2):
        return -1
    # 如果hash长度相同遍历长度
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n + 1
    return n


def init():
    dir_path = 'D:/Download/新建文件夹 (2)/风景日常/'
    res = get_file_list(dir_path)
    img_arr = []
    index = 0
    for item in res:
        img_arr = []
        index += 1
        dir_img_path = dir_path + item
        print(dir_img_path)
        img_list = get_file_list(dir_img_path)
        img_list.sort(key=lambda x: int(
            x[x.rfind('-')+1 if(x.rfind('_') == -1) else x.rfind('_')+1:x.rfind('.')]))
        for img in img_list:
            x = dir_img_path + '/' + img
            img_hash = get_img_hash(x)
            # print(img, img_hash)
            img_arr.append({'img': img, 'hash': str(img_hash)})
            time.sleep(0.01)
        #     break
        # break
        if(index > 3):
            break

    for item1 in img_arr:
        print()
        for item2 in img_arr:
            res = campHash(item1['hash'], item2['hash'])
            if(res < 17 and res > 0):
                print(item1, item2, res)
            time.sleep(0.01)


init()
