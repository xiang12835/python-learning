# coding=utf-8

"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def dfs(i, visited, M):
            for j in range(len(M)):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j, visited, M)

        visited = set()
        cnt = 0
        for i in range(len(M)):
            if i not in visited:
                dfs(i, visited, M)
                cnt += 1
        return cnt


class Solution1:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """ DFS
        T：O(n^2)，其中 n 是城市的数量。需要遍历矩阵 n 中的每个元素。
        S：O(n)，其中 n 是城市的数量。需要使用数组 visited 记录每个城市是否被访问过，数组长度是 n，递归调用栈的深度不会超过 n。
        """

        n = len(isConnected)
        visited = set()

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count

