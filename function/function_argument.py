# coding=utf-8


'''Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''


# 1)位置参数

# 2)默认参数

# 默认参数有个最大的坑，演示如下：
def add_end(L=[]):
    L.append('END')
    return L

print add_end()
print add_end()

# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！


# 要修改上面的例子，我们可以用None这个不变对象来实现：

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end()
print add_end()


# 3)可变参数


# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([1,2,3]) # 但是调用的时候，需要先组装出一个list或tuple
print calc([1,2,3,4,5])


def calc1(*num): # 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum

print calc1(1,2,3) # 利用可变参数，调用函数的方式可以简化成这样
print calc1(1,2,3,4,5)


# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1,3,5]
print calc1(nums[0], nums[1], nums[2]) # 这种写法当然是可行的，问题是太繁琐
print calc1(*nums) # 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去


# 4)关键字参数
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra) # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


# 5)命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# def person(name, age, *, city, job):
#     print(name, age, city, job)
#
# person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# person('Jack', 24, city='Beijing', job='Engineer')


# 6)参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的



'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''


# 比如定义一个函数，包含上述若干种参数：

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b = ', b, 'c =', c, 'args =', args, 'kw =', kw)

# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
# f2(1, 2, d=99, ext=None)

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
# f2(*args, **kw)
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
