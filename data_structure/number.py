# coding=utf-8


dec = 2147483647
b = bin(dec)
o = oct(dec)
h = hex(dec)


print "十进制数为：", dec
print "转换为二进制为：", b
print "转换为八进制为：", o
print "转换为十六进制为：", h


print "二进制转换为十进制：", int(b, 2)
print "八进制转换为十进制：", int(o, 8)
print "十六进制转换为十进制：", int(h, 16)
