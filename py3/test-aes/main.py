# import base64
# import os
# from Crypto import Random
# from Crypto.Cipher import AES

IV = 'IMGy92137kxhxabI'
KEY = 'I884417AYxOK0123'

from Caoliu1024 import Caoliu1024 

txt_url="https://img.boliwenshidapeng.com/aes/20210202/850f7297ec789786a81a952ac0c45ea4.png.txt"
txt_url = "https://img.boliwenshidapeng.com/aes/20201219/153abc066beab9b867b95c32369a5d3b.jpeg.txt"
txt_url="https://img.boliwenshidapeng.com/aes/20210116/1736bd9e747779d47514b4aa02a85f61.jpeg.txt"
txt_url="https://img.boliwenshidapeng.com/aes/20210205/b30a64a361787f8bcdc7459b74bc4e87.jpg.txt"
cl=Caoliu1024()
cl.start(txt_url)


# encrypt_data = u"8NXF5b/pWJGlWr66TSl3c9nJBTEUkz4tsiqfVQ0IW20="

# cipher = AES.new(KEY, AES.MODE_CBC, IV)
# result = base64.b64decode(encrypt_data)
# a = cipher.decrypt(result)

# a = a.decode("utf-8", "ignore")
# a = a.rstrip("\n")
# a = a.rstrip("\t")
# a = a.rstrip("\r")
# a = a.rstrip("\x06")
# print("\n", "data:", a)


# class AES_encrypt_decrypt(object):
#     def __init__(self, key):
#         self.key = key.encode('utf-8')
#         self.mode = AES.MODE_CFB

#     # 加密函数，采用CFB方式，text明文没有长度限制
#     def encrypt(self, text):
#         text = text.encode('utf-8')
#         #注意，这里Python3.6下用AES传递key时必须要转换成2进制，key前面要加'b'
#         crypto = AES.new(self.key, self.mode, b'woshigongyao6666')
#         # 这里密钥key 长度必须为16（AES-128）,
#         # 24（AES-192）,或者32 （AES-256）Bytes 长度
#         # 目前AES-128 足够目前使用
#         self.ciphertext = crypto.encrypt(text)
#         # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
#         # 所以这里统一用base64转化为字符串
#         return str(base64.encodebytes(self.ciphertext), encoding='utf-8')

#     # 解密
#     def decrypt(self, text):
#         crypto = AES.new(self.key, self.mode, b'woshigongyao6666')
#         plain_text = crypto.decrypt(
#             base64.decodebytes(text.encode(encoding='utf-8')))
#         return bytes.decode(plain_text)


# if __name__ == '__main__':
#     # 初始化密钥
#     sql = AES_encrypt_decrypt('woshisiyao666888')
#     text = '你好!'
#     e = sql.encrypt(text)  # 加密
#     d = sql.decrypt(e)  # 解密
#     print("原文：" + '\n' + text + '\n')
#     print("加密结果:" + '\n' + e)
#     print("解密结果:" + '\n' + d)


# def pkcs7padding(text):
#     """
#     明文使用PKCS7填充
#     最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
#     :param text: 待加密内容(明文)
#     :return:
#     """
#     bs = AES.block_size  # 16
#     length = len(text)
#     bytes_length = len(bytes(text, encoding='utf-8'))
#     # tips：utf-8编码时，英文占1个byte，而中文占3个byte
#     padding_size = length if (bytes_length == length) else bytes_length
#     padding = bs - padding_size % bs
#     # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
#     padding_text = chr(padding) * padding
#     return text + padding_text


# def pkcs7unpadding(text):
#     """
#     处理使用PKCS7填充过的数据
#     :param text: 解密后的字符串
#     :return:
#     """
#     try:
#         length = len(text)
#         unpadding = ord(text[length - 1])
#         return text[0:length - unpadding]
#     except Exception as e:
#         print(e)
#         pass


# def aes_encode(key, content):
#     """
#     AES加密
#     key,iv使用同一个
#     模式cbc
#     填充pkcs7
#     :param key: 密钥
#     :param content: 加密内容
#     :return:
#     """
#     key_bytes = bytes(key, encoding='utf-8')
#     iv = key_bytes
#     iv = b'IMGy92137kxhxabI'
#     key_bytes = b'I884417AYxOK0123'
#     cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
#     # 处理明文
#     content_padding = pkcs7padding(content)
#     # 加密
#     aes_encode_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
#     # 重新编码
#     result = str(base64.b64encode(aes_encode_bytes), encoding='utf-8')
#     return result


# def aes_decode(key, content):
#     """
#     AES解密
#      key,iv使用同一个
#     模式cbc
#     去填充pkcs7
#     :param key:
#     :param content:
#     :return:
#     """
#     try:
#         key_bytes = bytes(key, encoding='utf-8')
#         iv = key_bytes
#         iv = b'IMGy92137kxhxabI'
#         key_bytes = b'I884417AYxOK0123'
#         cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
#         # base64解码
#         aes_encode_bytes = base64.b64decode(content)
#         # 解密
#         aes_decode_bytes = cipher.decrypt(aes_encode_bytes)
#         # 重新编码
#         result = str(aes_decode_bytes, encoding='utf-8')
#         # 去除填充内容
#         result = pkcs7unpadding(result)
#     except Exception as e:
#         print(e)
#         pass
#     if result == None:
#         return ""
#     else:
#         return result


# import requests
# txt_url = "https://img.boliwenshidapeng.com/aes/20201219/153abc066beab9b867b95c32369a5d3b.jpeg.txt"
# txt_url = "https://img.boliwenshidapeng.com/aes/20210202/850f7297ec789786a81a952ac0c45ea4.png.txt"
# file_name = txt_url[txt_url.rfind("/") + 1:txt_url.rfind(".")]
# res = requests.get(txt_url, stream=False)
# # print(res.content)

# key = '12345678g01234ab'

# # 对英文加密
# data = 'Hello!'
# data = '111'
# mi = aes_encode(key, data)
# mi = res.content
# # print(mi)
# # 解密
# img_base64 = aes_decode(key, mi)
# print(img_base64[:100] + "(......)" + img_base64[len(img_base64) - 100:])
# img_base64 = img_base64[img_base64.find(",") + 1:]
# data = base64.b64decode(img_base64)

# # print(type(data))  # <class 'bytes'>
# # hex_imgdata = ''.join(["%02X" % x for x in data]).strip()
# # print(type(hex_imgdata))  # <class 'str'>

# with open(file_name, 'wb') as f:
#     f.write(data)

# # 中英文混合加密
# data = 'Hello 哈喽'
# aes_encode_mixed = aes_encode(key, data)
# print(aes_encode_mixed)
# # 解密
# print(aes_decode(key, aes_encode_mixed))
