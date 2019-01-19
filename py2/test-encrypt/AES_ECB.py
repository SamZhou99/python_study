#!/usr/bin/env python
# coding=utf-8

import base64
from Crypto.Cipher import AES


STR1 = '18587951209'
STR2 = '3sQetQjp7O7iO4HrwAlYQw=='
KEY = 'FZgC3e90tWjQczjW'
BS = AES.block_size


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s):
    return s[0:-ord(s[-1])]

# 36进制转换表


def get_table():
    # table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
    table = '0123456789abcdefghijklmnopqrstuvwxyz'
    length = len(table)
    return {'table': table, 'length': length}

# 进制编码


def encode_binary(n):
    t = get_table()
    table = t['table']
    length = t['length']
    result = []
    temp = int(n)
    if 0 == temp:
        result.append('0')
    else:
        while 0 < temp:
            result.append(table[temp % length])
            temp /= length
    return ''.join([x for x in reversed(result)])

# 进制解码


def decode_binary(str):
    t = get_table()
    table = t['table']
    length = t['length']
    result = 0
    for i in xrange(len(str)):
        result *= length
        s = str[i]
        index = table.find(s)
        result += index
    return result

# base编解码


def test_base64():
    s = 'ABC'
    e = base64.b64encode(s)
    d = base64.b64decode(e)
    return (s, e, d)

# AES编解码


def encryptAES(text):
    text = encode_binary(text)
    text = pad(text)
    text = AES.new(KEY, AES.MODE_ECB).encrypt(text)
    # text = text.encode('hex')
    text = base64.b64encode(text)
    return text


def decryptAES(text):
    text = base64.b64decode(text)
    text = AES.new(KEY, AES.MODE_ECB).decrypt(text)
    text = unpad(text)
    text = decode_binary(text)
    return text


def test_AES():
    phone = STR1
    print(phone)

    phone = encryptAES(phone)
    print(phone)
    
    phone = decryptAES(phone)
    print(phone)

# 初始化


def init():
    test_AES()


init()
