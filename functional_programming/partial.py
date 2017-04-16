# coding=utf-8

'''
简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
'''


# 转换大量的二进制字符串
import functools
int2 = functools.partial(int, base=2)

print int2('111110000')

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
print int2('1010')
kw = { 'base':2 }
print int('1010', **kw)
