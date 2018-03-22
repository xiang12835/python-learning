# coding=utf-8


def bin_search(l, n):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] == n:
            return mid
        elif l[mid] < n:
            left = mid + 1
        else:
            right = mid - 1

    return -1
