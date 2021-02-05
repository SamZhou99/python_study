import requests
import base64
import os
from Crypto.Cipher import AES


class Caoliu1024(object):

    # 初始化
    def __init__(self):
        self.key = b"I884417AYxOK0123"
        self.iv = b"IMGy92137kxhxabI"
        self.mode = AES.MODE_CBC

    # 添加填充
    def __pkcs7padding(self, text):
        bs = AES.block_size  # 16
        length = len(text)
        bytes_length = len(bytes(text, encoding='utf-8'))
        # tips：utf-8编码时，英文占1个byte，而中文占3个byte
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
        padding_text = chr(padding) * padding
        return text + padding_text

    # 解压填充
    def __pkcs7unpadding(self, text):
        try:
            length = len(text)
            unpadding = ord(text[length - 1])
            return text[0:length - unpadding]
        except Exception as e:
            print(e)
            pass

    # 加密
    def __aes_encode(self, content):
        cipher = AES.new(self.key, self.mode, self.iv)
        content_padding = self.__pkcs7padding(content)
        aes_encode_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
        result = str(base64.b64encode(aes_encode_bytes), encoding='utf-8')
        return result

    # 解密
    def __aes_decode(self, content):
        try:
            cipher = AES.new(self.key, self.mode, self.iv)
            aes_encode_bytes = base64.b64decode(content)
            aes_decode_bytes = cipher.decrypt(aes_encode_bytes)
            result = str(aes_decode_bytes, encoding='utf-8')
            result = self.__pkcs7unpadding(result)
        except Exception as e:
            print(e)
            pass
        if result == None:
            return ""
        else:
            return result

    # 开始
    def start(self, txt_url):
        self.txt_url = txt_url
        file_name = txt_url[txt_url.rfind("/") + 1:txt_url.rfind(".")]

        res = requests.get(txt_url, stream=False)
        txt_base64 = res.content
        # self.__aes_encode(txt_base64)
        img_base64 = self.__aes_decode(txt_base64)
        img_base64 = img_base64[img_base64.find(",") + 1:]
        data = base64.b64decode(img_base64)
        
        with open(file_name, 'wb') as f:
            f.write(data)
        # print(img_base64[:100] + "(......)" + img_base64[len(img_base64) - 100:])
        return data
