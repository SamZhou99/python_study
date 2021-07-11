from skimage import io, data

img = data.astronaut()

# 获取图片的像素
pixel = img[20, 10, 2]
print(pixel)

i = 10
j = 20
img[i, :] = img[j, :]      # 将第 j 行的数值赋值给第 i 行
img[:, i] = 100          # 将第 i 列的所有数值设为 100
img[:100, :50].sum()     # 计算前 100 行、前 50 列所有数值的和
img[50:100, 50:100]      # 50~100 行，50~100 列（不包括第 100 行和第 100 列）
img[i].mean()           # 第 i 行所有数值的平均值
img[:, -1]               # 最后一列
# img[-2, :] (or img[-2])   # 倒数第二行


io.imshow(img)
io.show()
