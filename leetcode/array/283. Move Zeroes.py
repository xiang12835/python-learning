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

        T: O(n)
        S: O(1)

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

        T: O(n)
        S: O(1)
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

class Solution3(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        双指针

        快速排序的思想:

        快速排序首先要确定一个待分割的元素做中间点x，然后把所有小于等于x的元素放到x的左边，大于x的元素放到其右边。
        这里我们可以用0当做这个中间点，把不等于0(注意题目没说不能有负数)的放到中间点的左边，等于0的放到其右边。
        这的中间点就是0本身，所以实现起来比快速排序简单很多，我们使用两个指针i和j，只要nums[i]!=0，我们就交换nums[i]和nums[j]

        T: O(n)
        S: O(1)
        """
        if not nums:
            return 0

        # 两个指针i和j
        n = len(nums)
        j = 0
        for i in range(n):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
