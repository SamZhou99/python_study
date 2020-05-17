import requests


class Download():

    def __init__(self, downloadUrl, fileName):
        super(Download, self).__init__()
        self.downloadUrl = downloadUrl
        self.fileName = fileName
        Download.downloadFile(self.downloadUrl, self.fileName)

    def downloadFile(downloadUrl, fileName):
        Chunk_Size = 512
        res = requests.get(downloadUrl, stream=True)
        with open(fileName, 'wb') as f:
            for chunk in res.iter_content(chunk_size=Chunk_Size):
                if chunk:
                    f.write(chunk)

    def getString(self):
        return '下载 ' + self.downloadUrl
