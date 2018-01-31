# coding=utf-8

""" 定义
官方解释：

os： This module provides a portable way of usingoperating system dependent functionality.

翻译：提供一种方便的使用操作系统函数的方法。
"""

""" os 常用方法
os.remove()删除文件
os.rename()重命名文件
os.walk()生成目录树下的所有文件名
os.chdir()改变目录
os.mkdir/makedirs创建目录/多层目录
os.rmdir/removedirs删除目录/多层目录
os.listdir()列出指定目录的文件
os.getcwd()取得当前工作目录
os.chmod()改变目录权限
os.path.basename()去掉目录路径，返回文件名
os.path.dirname()去掉文件名，返回目录路径
os.path.join()将分离的各部分组合成一个路径名
os.path.split()返回（dirname(),basename())元组
os.path.splitext()(返回filename,extension)元组
os.path.getatime\ctime\mtime分别返回最近访问、创建、修改时间
os.path.getsize()返回文件大小
os.path.exists()是否存在
os.path.isabs()是否为绝对路径
os.path.isdir()是否为目录
os.path.isfile()是否为文件
"""

import os

path = "/tmp"

os.path.realpath(path)
# /private/tmp
os.path.dirname(path)
# '/'
os.path.basename(path)
# 'tmp'
os.path.abspath(path)
# '/tmp'
