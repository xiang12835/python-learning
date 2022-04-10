# coding=utf-8

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """ 二分法 + 暴力
        https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-de-zui--16/

        可重复

        T: O(logN)
        S: O(1)
        """
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1 # 暴力缩小范围

        return nums[l]
