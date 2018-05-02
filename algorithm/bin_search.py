# coding=utf-8


def bin_search(l, n):
    # Time: O(log(n))
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if n == l[mid]:
            return mid
        elif n > l[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


""" 二分查找

二分搜索算法的复杂度是对数级别的，意味着用bisect来搜索包含一百万个元素的列表，与用index来搜索包含14个元素的列表，所耗的时间差不多

"""


import time

t0 = time.time()
x = list(range(10**6))
i = x.index(991234)
print i

t1 = time.time()
print t1 - t0


from bisect import bisect_left
j = bisect_left(x, 991234)
print j

t2 = time.time()
print t2 - t1

