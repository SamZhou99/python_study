

from skimage import io, data, color

img = data.astronaut()

# # 将宇航员图片进行二值化，像素值大于128的变为1, 否在变为0
# img_gray = color.rgb2gray(img)
# rows, cols = img_gray.shape

# for i in range(rows):
#     for j in range(cols):
#         if (img_gray[i, j] <= 0.5):
#             img_gray[i, j] = 0
#         else:
#             img_gray[i, j] = 1
# io.imshow(img_gray)

# 使用color模块的rgb2gray()函数，将彩色三通道图片转换为灰度图片，转换结果为float64类型的数组，范围在[0,1]之间
img_idx_modified = img[:, :, 0] > 170
print(img_idx_modified)
img[img_idx_modified] = [0, 255, 0]
io.imshow(img)


io.show()
