"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        length = len(nums)
        for i in xrange(length):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index, nums[:index]


if __name__ == '__main__':
    s = Solution()
    print s.removeElement([3,2,1,3,3], 3)
