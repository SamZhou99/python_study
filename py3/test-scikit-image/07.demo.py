from skimage import io, data

img = data.astronaut()
# 裁剪图片
partial_img = img[50:150, 170:270, :]
io.imshow(partial_img)
io.show()