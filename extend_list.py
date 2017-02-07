# coding=utf-8


def extend_list(val, lst=[]):
    lst.append(val)
    return lst

l1 = extend_list(10)
l2 = extend_list(123, [])
l3 = extend_list('a')

print l1
print l2
print l3


# 出现的问题
def add_end(L=[]):
    L.append('END')
    return L

print add_end()
print add_end()


# 原因：Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# 解决：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end()
print add_end()

# 定义默认参数要牢记一点：默认参数必须指向不变对象
