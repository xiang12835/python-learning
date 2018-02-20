# coding=utf-8

''' range
函数说明：range([start,] stop[, step])，根据start与stop指定的范围以及step设定的步长，生成一个列表。
'''

print range(10)
print range(2,10)
print range(2,10,2)


''' xrange 
函数说明：和range 的用法完全相同，但是返回的是一个生成器。 
'''

print xrange(10)
print xrange(2,10)
print xrange(2,10,2)


'''
但是要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间，这两个基本上都是在循环的时候用。
'''

r = range(0,50)
print r
print type(r)
print r[0],r[49]


xr = xrange(0,50)
print xr
print type(xr)
print xr[0],xr[49]

print list(xr) == r


'''
再循环中尽量使用 xrange 这样性能可以得到提高，除非你要返回一个列表
'''

for i in range(0, 50): print i

for i in xrange(0, 50): print i


