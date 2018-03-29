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
