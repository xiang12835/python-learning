# coding=utf-8

"""

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?

"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        双指针

        三路快速排序方法

        设置三个 l, r, i 定义：nums[0...l] == 0，nums[l+1...i-1] = 1，nums[r...n-1] == 2，遍历一遍改数列保持这个定义。

        T: O(N)
        S: O(1)
        """

        lt = -1
        gt = len(nums)
        i = 0
        while i < gt:
            if nums[i] == 0:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            elif nums[i] == 2:
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
            else:
                i += 1
            print i, nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print nums
