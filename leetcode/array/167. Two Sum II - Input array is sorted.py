"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


# o(n*n)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 2:
            return []

        length = len(numbers)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        return []


# two-pointer; o(n)
class Solution1(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 2:
            return []

        l, r = 0, len(numbers) - 1

        while l < r:

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1


# dictionary
class Solution2(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for i, num in enumerate(numbers):
            if target - num in d.keys():
                return [d[target - num] + 1, i + 1]
            else:
                d[num] = i


# binary search; O(n*log n)
class Solution3(object):
    def twoSum(self, numbers, target):
        for i in xrange(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1
