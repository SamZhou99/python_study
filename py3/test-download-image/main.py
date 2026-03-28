import requests

img_url = 'https://ai-bot.cn/wp-content/uploads/2023/12/seaart-ai-website.png'

def DownloadImg(imgUrl, imgSaveName):
    res = requests.get(imgUrl, timeout=2)
    with open(imgSaveName, "wb") as f:
        f.write(res.content)
        f.close()


DownloadImg(img_url, './111.jpg')
