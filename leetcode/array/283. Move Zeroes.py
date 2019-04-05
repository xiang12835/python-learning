# coding=utf-8

"""
 Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = []
        for n in nums:
            if n != 0:
                r.append(n)

        nums[:] = r + [0] * (len(nums) - len(r))


class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        一旦遇到不是0的就把它往前移动，移动非0完成，剩下的全部填0，看例子

        """
        idx = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1

        for j in xrange(idx, len(nums)):
            nums[idx] = 0
            idx += 1


class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        快慢指针
        """
        slow = 0
        fast = 0

        n = len(nums)
        while fast < n:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while slow < n:
            nums[slow] = 0
            slow += 1
