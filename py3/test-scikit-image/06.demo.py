from skimage import io, data
import numpy as np

img = data.astronaut()

# 随机生成5000个椒盐点
rows, cols, dims = img.shape

for i in range(9000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255

io.imshow(img)
io.show()