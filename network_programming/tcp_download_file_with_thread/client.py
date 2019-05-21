# coding=utf-8

from socket import socket
from json import loads
from base64 import b64decode
import os

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

def main():

    client = socket()
    client.connect(('192.168.1.102', 8089))
    # 定义一个保存二进制数据的对象
    received_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        received_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(received_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')

    filepath = os.path.join(PROJECT_ROOT, filename)

    print(filepath)

    with open(filepath, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存.')


if __name__ == '__main__':
    main()

