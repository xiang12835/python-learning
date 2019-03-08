"""

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        首先去重复，时间O(N),然后将所有元素都放到一个字典中，这样判断一个数字的后续在不在这个字典中，如果存在就一直判断下去，每次判断只要O(1)。
        """
        ss = set(nums)

        r = 0
        for n in nums:
            if n - 1 not in nums:
                x = n + 1
                while x in nums:
                    x += 1

                r = max(r, x - n)

        return r
