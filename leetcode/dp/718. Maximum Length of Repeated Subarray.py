# coding=utf-8

"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

"""

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int

        T：O(N×M)
        S：O(N×M)
        """
        m = len(A)
        n = len(B)
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans