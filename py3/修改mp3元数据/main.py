import eyed3

mp3_file = eyed3.load("王杰 - 一无所有.mp3")
title = mp3_file.tag.title
mp3_file.tag.title = "测试一下"
mp3_file.tag.save()
print(title)
