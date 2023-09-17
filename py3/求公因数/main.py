# 求最大公因数
def getGCD(w, h):
    i = 0
    isZ = w > h
    W, H = (w, h) if isZ else (h, w)
    w, h = W, H
    while i < 10:
        i = i + 1
        m = w % h
        # print("{}, {}, {}, {}".format(i, w, h, m))
        if m == 0:
            # print("是否需要反转", isZ)
            return h, isZ
        else:
            w = h
            h = m
    return 0


# 求比例
def getScale(w, h):
    gcd, _ = getGCD(w, h)
    return int(w / gcd), int(h / gcd)


print(getScale(3840, 2160))  # 最大公因数 240
print(getScale(1024, 768))  # 最大公因数 256
print(getScale(15563, 19109))  # 最大公因数 197
print(getScale(9, 16))  # 最大公因数 1
