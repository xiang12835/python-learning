# 　coding=utf-8

# 定义: 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
# 好处: 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。


'''以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数'''
ls = map(lambda x:x*x, [1,2,3,4,5])
print ls


'''匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数'''
f = lambda x:x*x
print f(5)


'''把匿名函数作为返回值返回'''
def build(x, y):
    return lambda :x*x + y*y

print build(3, 4)


# 面试题
def multipliers():
    return [lambda x: i*x for i in range(4)]

print [m(2) for m in multipliers()]
# [6, 6, 6, 6]

'''
上述问题产生的原因是Python闭包的延迟绑定。这意味着内部函数被调用时，参数的值在闭包内进行查找。
因此，当任何由multipliers()返回的函数被调用时，i的值将在附近的范围进行查找。
那时，不管返回的函数是否被调用，for循环已经完成，i被赋予了最终的值3。
'''

# 解决
# 一种解决方法就是用Python生成器。

def multipliers():
  for i in range(4):
      yield lambda x : i * x

print [m(2) for m in multipliers()]

