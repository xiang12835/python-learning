# coding=utf-8

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        排序 + 贪心

        T: mlogm + nlogn
        S: logm + logn
        """

        g.sort()
        s.sort()

        g_length = len(g)
        s_length = len(s)

        i = 0  # 孩子胃口
        j = 0  # 饼干

        r = 0
        while (i < g_length and j < s_length):
            if g[i] <= s[j]:  # 满足胃口，把饼干喂给小朋友
                r += 1
                i += 1
                j += 1
            else:  # 不满足胃口，查看下一个饼干
                j += 1

        return r
