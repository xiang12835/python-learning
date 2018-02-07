'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(list(set(nums)))


class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0
        length = len(nums)
        for i in range(1, length):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1, 1, 2, 2, 3])

    s1 = Solution1()
    print s1.removeDuplicates([1, 1, 2, 2, 3])
