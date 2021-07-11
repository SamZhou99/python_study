from skimage import io, data, color

img = data.astronaut()

# 图片灰度
R = img[:, :, 0]

# 图片灰度
# R=gray=color.rgb2gray(img)

io.imshow(R)
io.show()
