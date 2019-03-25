# coding=utf-8

"""

6、给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如 果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

"""


class Solution(object):
    def searchInsert(self, l, n):
        left = 0
        right = len(n)
        while left <= right:
            mid = left + (right-left) >> 2
            if n < l[mid]:
                right = mid - 1

            elif n > l[mid]:
                left = mid + 1

            else:

                return mid
