# coding=utf-8

classmates = ['Michael', 'Bob', 'Tracy']
print classmates

print len(classmates)

print classmates[1]

print classmates[-1]

classmates.append('Adam') # 往list中追加元素到末尾
print classmates

classmates.insert(1, 'Jack') # 可以把元素插入到指定的位置
print classmates

classmates.pop() # 要删除list末尾的元素
print classmates

classmates.pop(1) # 要删除指定位置的元素
print classmates

classmates[1] = 'Sarah' # 要把某个元素替换成别的元素
print classmates

L = ['Apple', 123, True] # list里面的元素的数据类型也可以不同
print L

s = ['python', 'java', ['asp', 'php'], 'scheme'] # list元素也可以是另一个list
print len(s)

L = []
print len(L)


# 列表切割
#
# list[start:end:step]
# 如果从列表开头开始切割，那么忽略 start 位的 0，例如list[:4]
# 如果一直切到列表尾部，则忽略 end 位的 0，例如list[3:]
# 切割列表时，即便 start 或者 end 索引跨界也不会有问题
# 列表切片不会改变原列表。索引都留空时，会生成一份原列表的拷贝
a = [1, 2, 3]
b = a[:]
assert b == a and b is not a  # true


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print 'L[0:3] =', L[0:3]
print 'L[:3] =', L[:3]
print 'L[1:3] =', L[1:3]
print 'L[-2:] =', L[-2:]

R = list(range(100))
print 'R[:10] =', R[:10]
print 'R[-10:] =', R[-10:]
print 'R[10:20] =', R[10:20]
print 'R[:10:2] =', R[:10:2]
print 'R[::5] =', R[::5]

print "R[::-1] =", R[::-1]

# 列表排序
l1 = [2,1,4,3,2]
print sorted(l1)  # 升序
print sorted(l1, reverse=True)  # 降序


# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
print sorted(l1, key=lambda el:el)  # 升序
print sorted(l1, key=lambda el:-el)  # 降序

l2 = [2,1,4,3,2]
l2.sort()
print l2

l3 = [2,1,4,3,2]
l3.sort(reverse=True)
print l3

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
people.sort(key=lambda (h, k): (-h, k))

print people

# 列表反转
l4 = [2,1,4,3,2]
l4.reverse()
print l4

l5 = [2,1,4,3,2]
print list(reversed(l5))

print l5[::-1]


# count() 方法用于统计某个元素在列表中出现的次数。

numbers = [2,1,4,3,2]
print numbers.count(2)


import collections
d = collections.Counter(numbers)
print d


# 如何以就地操作方式打乱一个列表的元素？
mylist = [1,2,3,4,5,6,7,8,9]
from random import shuffle
shuffle(mylist)

print mylist
