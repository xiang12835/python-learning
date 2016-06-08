# coding=utf-8

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算,
其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''


# 比方说对一个序列求和，就可以用reduce实现
from functools import reduce
def add(x,y):
    return x+y

print reduce(add, [1,2,3,4,5])


# 如果要把序列[1,2,3,4,5]变换成整数12345
def fn(x,y):
    return x*10 + y

print reduce(fn, [1,2,3,4,5])


# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数
def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

print reduce(fn, map(char2num, '13579'))


# 整理成一个str2int的函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print str2int('24680')


# 还可以用lambda函数进一步简化
# def char2num(s):
#     return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

def str2int(s):
    return reduce(lambda x,y:x*10+y, map(char2num, s))

print str2int('1536')


# 练习1: Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
# from functools import reduce
def prod(L):
    return reduce(lambda x,y : x*y, L)

print prod([1,2,3,4,5])


# 练习2: 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# 法一
# from functools import reduce
def findpoint(s, index):
    while index:
        if s[index] == '.':
            return index
        index -= 1

def str2float(s):
    index = len(s) - 1
    num = index - findpoint(s, index)
    s = s.split('.')[0] + s.split('.')[1]
    return float(str2int(s))/pow(10, num)

print str2float('13.45')


# 法二
def str2float0(s):
    sn = s.split('.')[0] + s.split('.')[1]
    def char2num(sn):
        return {'0':0 ,'1':1, '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[sn]
    def str2int(sn):
        return reduce(lambda x,y : x*10+y, map(char2num, sn))
    return float(str2int(sn))/pow(10, len(s)-1-s.index('.'))

print str2float0('123.456')
