# coding=utf-8

"""
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

"""


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool

        T: O(n)
        S: O(1)
        """
        ss = sum(A)
        if ss % 3 != 0:
            return False

        target_sum = ss / 3
        n = len(A)
        i = 0
        cur_sum = 0

        while i < n:
            cur_sum += A[i]
            if cur_sum == target_sum:
                break
            i += 1

        if cur_sum != target_sum:
            return False

        j = i + 1
        while j + 1 < n:  # 注意，因为只算前两个数组，第三个不用算，但是不能为空。
            cur_sum += A[j]
            if cur_sum == target_sum * 2:
                return True
            j += 1

        return False

