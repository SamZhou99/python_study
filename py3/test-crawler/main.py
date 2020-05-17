import urllib.request
import requests
import chardet


ITEM_URL = 'http://www.ik123.com/mp3-dj/ik123_{id}.html'
ITEM_IFRAME_URL = 'http://www.ik123.com/ik/p/?{furl}'
ITEM_MP4 = 'http://mp4.ik123.com/Dj_www.ik123.com/2010/{furl}?vsid=32c8b5efe1e2523036da74471ab03d9b&name=www.ik123.com'


def writeFile(filePath, text):
    f = open('./test.html', 'w')  # 若是'wb'就表示写二进制文件
    f.write(text)
    f.close()


def openIframeUrl(url):
    response = urllib.request.urlopen(url)
    htmlStr = response.read()
    charset = chardet.detect(htmlStr)['encoding']
    html = htmlStr.decode(charset)
    print('页面编码', charset)

    titleString = 'var musicName="'
    titleStart = html.find(titleString)
    titleEnd = html.find('";', titleStart)
    title = html[titleStart+len(titleString):titleEnd]
    print(title)

    furlString = 'var furl="'
    furlStart = html.find(furlString)
    furlEnd = html.find('";', furlStart)
    furl = html[furlStart+len(furlString):furlEnd]
    print(furl)

    furlFill = ITEM_IFRAME_URL.replace('{furl}', furl)
    print(furlFill)

    mp4Url = ITEM_MP4.replace('{furl}', furl.replace('.flv', '.mp4'))
    print(mp4Url)

    r = requests.get(mp4Url, stream=True)
    f = open('./'+title+'.mp4', 'wb')
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
    print('download over')


def openUrlById(id):
    url = ITEM_URL.replace('{id}', str(id))
    openIframeUrl(url)


def init():
    for i in range(3):
        id = 12254+i
        openUrlById(id)


init()

# // 第一步
# // var rid="12425";nextid="12426";
# // var mymp3="0";var strstr="1";
# // var musicName="墨尔本巴库露天豪情疯狂派对弹跳盛宴";
# // var rurl="/a/202004%2Fik123_2004A016.wma";
# // var zurl="202004%2Fik123_2004A016.wma";
# // var furl="202004%2Fik123_2004A016.flv";

# // 第二步
# // http://www.ik123.com/ik/p/?202004%2Fik123_2004A007.flv

# // 第三步
# http://mp4.ik123.com/Dj_www.ik123.com/2010/202004%2Fik123_2004A007.mp4?vsid=32c8b5efe1e2523036da74471ab03d9b&name=www.ik123.com
# http://mp4.ik123.com/Dj_www.ik123.com/2010/202001%2Fik123_2001F019.mp4?vsid=32c8b5efe1e2523036da74471ab03d9b&name=www.ik123.com
