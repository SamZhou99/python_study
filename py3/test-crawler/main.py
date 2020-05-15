import urllib.request
import chardet

response = urllib.request.urlopen('http://www.72dj.com/play/32853.htm')
htmlStr = response.read()
charset = chardet.detect(htmlStr)['encoding']
html = htmlStr.decode(charset)
print(charset)
print(html)

f = open('./test.html', 'w')  # 若是'wb'就表示写二进制文件
f.write(html)
f.close()
