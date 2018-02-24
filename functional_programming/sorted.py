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
