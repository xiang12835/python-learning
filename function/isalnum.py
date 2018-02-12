# coding=utf-8

"""
描述

Python isalnum() 方法检测字符串是否由字母和数字组成。
语法

isalnum()方法语法：

str.isalnum()

参数

无。

返回值

如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
"""

str = "this2009"  # 字符中没有空格
print str.isalnum()

str = "this is string example....wow!!!"
print str.isalnum()
