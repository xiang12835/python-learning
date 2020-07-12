# coding=utf-8

"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

"""

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        复杂度为: O(n^2)
        """

        if not nums:
            return []

        if len(nums) == 1:
            return [0]

        ans = []
        for i in range(len(nums)):
            cnt = 0
            for n in nums[i+1:]:
                if n < nums[i]:
                    cnt += 1
            ans.append(cnt)

        return ans


import bisect
class Solution1(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        对于每个元素而言，右边的所有元素已经存放在sorted_nums中，并且排好序。可以直接使用bisect.bisect_left找到对应的元素在sorted_nums的下标。他的下标表示的就是在sorted_nums中比他小的元素的个数。把他一次添加到ans中去。

        时间复杂度：第一轮循环遍历所有元素o(n)，第二轮循环使用二分检索o(logn)。综合来说是o(nlogn)。
        空间复杂度：需要创建一个sorted_nums来记录排序好的右边元素。所以是：o(n)。

        """

        if not nums:
            return []

        sorted_nums = []
        ans = []
        for n in nums[::-1]:
            index = bisect.bisect_left(sorted_nums, n)
            bisect.insort(sorted_nums, n)
            ans.append(index)
        return ans[::-1]


if __name__ == "__main__":
    print Solution().countSmaller([5,2,6,1])
