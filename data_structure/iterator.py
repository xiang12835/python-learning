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


# 使用生成器

''' 1
考虑使用生成器来改写直接返回列表的函数
'''

# 定义一个函数，其作用是检测字符串里所有 a 的索引位置，最终返回所有 index 组成的数组
def get_a_indexs(string):
    result = []
    for index, letter in enumerate(string):
        if letter == 'a':
            result.append(index)
    return result

# 用这种方法有几个小问题：
# 1）每次获取到符合条件的结果，都要调用append方法。但实际上我们的关注点根本不在这个方法，它只是我们达成目的的手段，实际上只需要index就好了，
# 2）返回的result可以继续优化
# 3）数据都存在result里面，如果数据量很大的话，会比较占用内存
# 因此，使用生成器generator会更好。生成器是使用yield表达式的函数，调用生成器时，它不会真的执行，而是返回一个迭代器，每次在迭代器上调用内置的next函数时，迭代器会把生成器推进到下一个yield表达式：

def get_a_indexs(string):
    for index, letter in enumerate(string):
        if letter == 'a':
            yield index

# 获取到一个生成器以后，可以正常的遍历它：

string = 'this is a test to find a\' index'
indexs = get_a_indexs(string)

# 可以这样遍历
for i in indexs:
    print(i)

# 或者这样
try:
    while True:
        print(next(indexs))
except StopIteration:
    print('finish!')

# 生成器在获取完之后如果继续通过 next() 取值，则会触发 StopIteration 错误
# 但通过 for 循环遍历时会自动捕获到这个错误

# 如果你还是需要一个列表，那么可以将函数的调用结果作为参数，再调用list方法

results = get_a_indexs('this is a test to check a')
results_list = list(results)
