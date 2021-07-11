from skimage import img_as_ubyte
from skimage import io, data, img_as_float, img_as_ubyte
import numpy as np

img = data.astronaut()

# 一张图片的像素值范围是[0,255], 因此默认类型是unit8, 可用如下代码查看数据类型：
print(img.dtype.name)


# 在上面的表中，特别注意的是float类型，它的范围是[-1,1]或[0,1]之间。一张彩色图片转换为灰度图后，它的类型就由unit8变成了float
dst = img_as_float(img)
print(dst.dtype.name)


# float转为uint8
img = np.array([0, 0.5, 1], dtype=float)
print(img.dtype.name)

dst = img_as_ubyte(img)
print(dst.dtype.name)
