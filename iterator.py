# coding=utf-8

# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

from collections import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)