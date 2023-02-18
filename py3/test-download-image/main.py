import requests

img_url = 'http://img.sejiazu.com:3027/Uploads/vod/2022-12-12/b11b971c-b39d-4469-9714-6f5d4630dc68.jpg'

def DownloadImg(imgUrl, imgSaveName):
    res = requests.get(imgUrl, timeout=2)
    with open(imgSaveName, "wb") as f:
        f.write(res.content)
        f.close()


DownloadImg(img_url, './111.jpg')
