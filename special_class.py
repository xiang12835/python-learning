# coding=utf-8

'''
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
'''

# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值
#
# for n in Fib():
#     print(n)


class Student(object):
    def __init__(self, name):
        self.name = name

print Student('Michael') # 打印出一堆<__main__.Student object at 0x109afb190>，不好看


class Student0(object):
    def __init__(self, name):
        self.name = name
    def __str__(self): # 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__ # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

print Student0('Michael')
s = Student0('Jack')
print s

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib1(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

f = Fib1()
print f[0]
print f[1]
print f[2]
print f[10]


class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib2()
print f[0:5]


# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
class Student1(object):

    def __init__(self):
        self.name = 'Michael'

    # def __getattr__(self, attr):
    #     if attr == 'score':
    #         return 99

    def __getattr__(self, attr): # 返回函数
        if attr == 'age':
            return lambda: 25

s = Student1()
print s.name
# print s.score
print s.age()


# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
class Student_call(object):
    def __init__(self, name):
        self.name = name

    def __call__(self): # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
        print('My name is %s.' % self.name)

s = Student_call('Michael')
s()

print callable(Student_call('Michael'))

print callable(max)

print callable([1, 2, 3])

print callable(None)

print callable('str')