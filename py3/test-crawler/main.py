import urllib.request
import chardet

response = urllib.request.urlopen('http://hsck7.com/vodplay/1314-1-1.html')
htmlStr = response.read()
charset = chardet.detect(htmlStr)['encoding']
html = htmlStr.decode(charset)
print(charset)
print(html)
