#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 作业：格式化秒数的小工具
# 提示：使用format和+


import random

num = random.randint(100, 10000)
hour = int(num/3600)
minute = num % 3600//60
second = num % 3600 % 60

result1 = "使用format打印：{}秒 = {}时{}分{}秒".format(num, hour, minute, second)
result2 = "使用字符串拼接打印：" + str(num) + "秒 = " + str(hour) + "时" + str(minute) + "分" + str(second) + "秒"
print(result1)
print(result2)
