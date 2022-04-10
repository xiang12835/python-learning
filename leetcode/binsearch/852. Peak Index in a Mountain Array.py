# coding=utf-8

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        枚举

        T: O(N)
        S: O(1)
        """
        res = -1
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                res = i
                break

        return res

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        二分查找

        T: O(logN)
        S: O(1)
        """

        l = 0
        r = len(arr) - 2 # 易错

        ans = 0
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] > arr[m+1]:
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans