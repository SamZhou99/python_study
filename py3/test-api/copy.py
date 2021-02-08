import copy

v01 = [1, 2, 3, 4, 5]


def demo1_copy():
    v02 = v01
    print("v01 = ?".format(id(v01)))
    print("v02 = ?".format(id(v02)))


demo1_copy()
