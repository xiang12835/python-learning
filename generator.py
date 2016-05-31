# coding=utf-8

# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

'''法一: 只要把一个列表生成式的[]改成()，就创建了一个generator'''
g = (x*x for x in range(10))
print g


'''如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值'''
print next(g)
print next(g)


'''使用for循环，因为generator也是可迭代对象'''
for n in g:
    print n


'''输出斐波那契数列的前N个数'''
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print b
        a,b = b,a+b
        n += 1
    return 'done'

fib(6)

'''法二: 使用yield将函数改成generator'''
def g_fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n += 1

f = g_fib(6)
for g in f:
    print g


'''练习: 杨辉三角'''
def triangles():
    t = [1]
    while True:
        yield t
        t.append(0)
        t = [t[i-1] + t[i] for i in range(len(t))]

n = 0
for t in triangles():
    print t
    n = n + 1
    if n == 10:
        break


