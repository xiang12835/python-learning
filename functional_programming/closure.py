# coding=utf-8

''' 函数的嵌套 + 返回一个函数 + 内部函数引用外部函数的变量
相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''


# 实现函数的计数器
def counter(a=0):
    cnt = [a]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one

num5 = counter(5)
print num5()
print num5()
print num5()


# 实现 a * x + b = y
def a_line(a, b):
    return lambda x:a*x+b

line1 = a_line(3,5)
print line1(10)


# 一个闭包问题
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print f1(), f2(), f3() #9 9 9 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。


# 解决:如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()

print f1(), f2(), f3()



