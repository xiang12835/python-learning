# coding=utf-8

'''
Python内建的filter()函数用于过滤序列
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
用filter()这个高阶函数，关键在于正确实现一个“筛选”函数
'''


# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

print list(filter(is_odd, [1,2,3,4,5,6,7,8,9]))


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print list(filter(not_empty, ['A', 'B', '', None, '  ']))  # filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list


# 用filter求素数

# # 1) 可以先构造一个从3开始的奇数序列
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# # 2) 定义一个筛选函数
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
# # 3) 定义一个生成器，不断返回下一个素数
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)  # _not_divisible(n)相当于lambda n: lambda x: x % n > 0
#
# # 4)打印1000以内的素数
# for n in primes():
#     if n < 20:
#         print(n)
#     else:
#         break


# 练习: 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
# 使用递归
def is_palindrome(n):
    s = str(n)
    if (len(s) == 0) or (len(s) == 1):
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

output = filter(is_palindrome, range(1, 1000))
print(list(output))