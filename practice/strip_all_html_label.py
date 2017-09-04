# coding=utf-8

import re


html = '<a href="http://www.jb51.net">脚本之家</a>,Python学习！'
dr = re.compile(r'<[^>]+>', re.S)
dd = dr.sub('', html)
print(dd)
