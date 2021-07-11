import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from skimage import io

# 显示一张本地图片
img = io.imread("./dog.jpg")
print(img.shape)

plt.imshow(img)
plt.show()