from PIL import Image
import matplotlib.pyplot as plt
import numpy as nps

image = Image.open('./test.jpg')  #读取图像
# plt.imshow(image) #显示图片

# plt.imshow(image.rotate(180))  #逆时针旋转180度
plt.imshow(image.resize((64, 64)))  #缩放

# # 转换灰度图像
# image_gray = image.convert('L')
# data = nps.array(image_gray)
# plt.imshow(image_gray)

# # 转换图像格式
# image.save('./test2.png')

# # 裁剪图片
# x, y = (300, 0)
# w, h = (600, 500)
# box = (x, y, x + w, y + h)
# region = image.crop(box)
# data = nps.array(region)
# plt.imshow(data)

plt.show()  #需要调用show()方法，不然图像只会在内存中而不显示出来
