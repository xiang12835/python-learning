# coding=utf-8

"""描述

sorted() 函数对所有可迭代的对象进行排序操作。

    sort 与 sorted 区别：

    sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

    list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

"""


"""语法

sorted 语法：

sorted(iterable[, cmp[, key[, reverse]]])

参数说明：

    iterable -- 可迭代对象。
    cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

"""

"""返回值

返回重新排序的列表。

"""

a = [5, 7, 6, 3, 4, 1, 2]
b = sorted(a)  # 保留原列表
print a
print b


L = [('b', 2), ('a', 4), ('c', 3), ('d', 1)]
print sorted(L, cmp=lambda x, y: cmp(x[1], y[1]))  # 利用cmp函数
print sorted(L, key=lambda x: x[1])  # 利用key

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

print sorted(students, key=lambda s: s[2])  # 按年龄排序
print sorted(students, key=lambda s: s[2], reverse=True)  # 按降序




# 练习:
# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 请用sorted()对上述列表分别按名字排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L1 = sorted(L, key=by_name)
print L1

# 再按成绩从高到低排序
def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score, reverse=True)
print L2



""" 史上最全关于sorted函数的10条总结

sorted 用于对集合进行排序（这里说的集合是对可迭代对象的一个统称，他们可以是列表、字典、set、甚至是字符串），它的功能非常强大，本文将深入浅出地介绍 sorted 的各种使用场景。

1、默认情况，sorted 函数将按列表升序进行排序，并返回一个新列表对象，原列表保持不变，最简单的排序

>>> nums = [3,4,5,2,1]
>>> sorted(nums)
[1, 2, 3, 4, 5]
2、降序排序，如果要按照降序排列，只需指定参数 reverse=True 即可

>>> sorted(nums, reverse=True)
[5, 4, 3, 2, 1]
3、如果要按照某个规则排序，则需指定参数 key， key 是一个函数对象，例如字符串构成的列表，我想按照字符串的长度来排序

>>> chars = ['Andrew', 'This', 'a', 'from', 'is', 'string', 'test']

>>> sorted(chars, key=len)
['a', 'is', 'from', 'test', 'This', 'Andrew', 'string']
len 是内建函数，sorted 函数在排序的时候会用len去获取每个字符串的长度来排序。 有些人可能使用匿名函数 key=lambda x: len(x) ，其实多此一举。

4、如果是一个复合的列表结构，例如由元组构成的列表，要按照元组中的第二个元素排序，那么可以用 lambda 定义一个匿名函数

>>> students = [('zhang', 'A'), ('li', 'D'), ('wang', 'C')]
>>> sorted(students, key=lambda x: x[1])
[('zhang', 'A'), ('wang', 'C'), ('li', 'D')]
这里将按照字母 A-C-D 的顺序排列。

5、如果要排序的元素是自定义类，例如Student类按照年龄来排序，则可以写成

>>> class Student:
         def __init__(self, name, grade, age):
             self.name = name
             self.grade = grade
             self.age = age
         def __repr__(self):
             return repr((self.name, self.grade, self.age))

>>> student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('lily', 'A', 12),
     Student('dave', 'B', 10), ]
>>> sorted(student_objects, key=lambda t:t.age)
[('dave', 'B', 10), ('jane', 'B', 12), ('lily', 'A', 12), ('john', 'A', 15)]
6、和数据库的排序一样，sorted 也可以根据多个字段来排序，例如我有先要根据age排序，如果age相同的则根据grade排序，则可以使用元组：

>>> sorted(student_objects, key=lambda t:(t.age, t.grade))
[('dave', 'B', 10), ('lily', 'A', 12), ('jane', 'B', 12), ('john', 'A', 15)]
7、前面碰到的排序场景都是建立在两个元素是可以互相比较的前提下，例如数值按大小比较， 字母按顺序比较，如果遇到本身是不可比较的，需要我们自己来定义比较规则的情况如何处理呢？

举个简单的例子：

>>> nums = [2, 1.5, 2.5, '2', '2.5']
>>> sorted(nums)
TypeError: '<' not supported between instances of 'str' and 'int'
一个整数列表中，可能有数字，字符串，在Python3中，字符串与数值是不能比较的，而Python2中任何类型都可以比较，这是两个版本中一个很大的区别：

# python2.7
>>> "2.5" > 2
True

# python3.6
>>> "2.5" > 2
TypeError: '>' not supported between instances of 'str' and 'int'
我们需要使用 functools 模块中的 cmp_to_key 来指定比较函数是什么。

import functools
def compare(x1, x2):
    if isinstance(x1, str):
        x1 = float(x1)
    if isinstance(x2, str):
        x2 = float(x2)

    return x1 - x2

>>>sorted(nums, key=functools.cmp_to_key(compare))
[1.5, 2, '2', 2.5, '2.5']
8、关于 sorted 函数，Python2和Python3之间的区别是Python2中的sorted 可以指定cmp关键字参数，就是当遇到需要自定义比较操作的数据可以通过 cmp=compare 来实现，不需要像Python3中还需要导入functools.cmp_to_key实现。

nums = [2, 1.5, 2.5, '2', '2.5']

def compare(x1, x2):
    if isinstance(x1, str):
        x1 = float(x1)
    if isinstance(x2, str):
        x2 = float(x2)
    return 1 if x1 - x2 > 0 else -1 if x1 - x2 < 0 else 0

>>> sorted(nums, cmp=compare)
[1.5, 2, '2', 2.5, '2.5']
其实，在Python2中，上面这种情况你不指定cmp，默认也会按照这种方式排序，记住，Python2中，任何东西（不同类型之间）都可以比较，而Python3只有同类型数据可以比较。

9、 对于集合构成的列表，有一种更高效的方法指定这个key

>>> from operator import itemgetter
>>> sorted(students, key=itemgetter(1))
[('zhang', 'A'), ('wang', 'C'), ('li', 'D')]
10、同样的，对于自定义类，也有一种更高效的方法指定key

>>> from operator import attrgetter
>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
如果参与排序的字段有两个怎么办，你可以这样：

>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
以上是关于 sorted 函数的全部。留给大家的作业：sorted 函数的实现原理是什么？



"""
