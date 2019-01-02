# coding=utf-8

"""

re.sub(pattern, repl, string, count=0, flags=0)

pattern：表示正则表达式中的模式字符串；

repl：被替换的字符串（既可以是字符串，也可以是函数）；

string：要被处理的，要被替换的字符串；

count：匹配的次数, 默认是全部替换


"""

import re

content = 'h!!e&ll##o'
# content = 'hello'
patten = '\+|=|,|&|%|#|@|!'

def strip_custom_str(patten, content):
    r = re.sub(patten, '', content)
    return r

print strip_custom_str(patten, content)


# course_name = 'h!!e&ll##o'
#
# exclude_str_list = ['+', '=', ',', '&', '%', '#', '@', '!']
#
# def strip_custom_str(course_name, exclude_str_list):
#     for c in course_name:
#         if c in exclude_str_list:
#             course_name = course_name.replace(c, '')
#
#     return course_name
#
# print strip_custom_str(course_name, exclude_str_list)


# print ''.join(exclude_str_list)


