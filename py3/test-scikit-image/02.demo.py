from skimage import io, data, data_dir

# 显示保存路径
print("示例图保存的路径：", data_dir)

# 自带的图片数据
img = data.hubble_deep_field()
io.imshow(img)
io.show()
