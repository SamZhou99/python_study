from skimage import io, data, color
import numpy as np

img = data.astronaut()

# #  RGB转为HSV
# hsv = color.convert_colorspace(img, 'RGB', 'HSV')
# io.imshow(hsv)


gray = color.rgb2gray(img)
rows, cols = gray.shape
labels = np.zeros([rows, cols])
for i in range(rows):
    for j in range(cols):
        if(gray[i, j] < 0.4):
            labels[i, j] = 0
        elif(gray[i, j] < 0.75):
            labels[i, j] = 1
        else:
            labels[i, j] = 2
dst = color.label2rgb(labels)
io.imshow(dst)


io.show()
