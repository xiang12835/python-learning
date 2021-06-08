# coding=utf-8

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        双指针 - 左右碰撞

        这道问题的暴力解法比「接雨水」那道题要其实好想得多：可以枚举以每个柱形为高度的最大矩形的面积。
        具体来说是：依次遍历柱形的高度，对于每一个高度分别向两边扩散，求出以当前高度为矩形的最大宽度多少。

        T：O(N**2)，这里 N 是输入数组的长度。
        S：O(1)。
        """
        n = len(heights)
        ans = 0

        for i in range(n):
            cur_height = heights[i]
            l = i
            while l > 0 and heights[l - 1] >= cur_height:
                l -= 1

            r = i
            while r < n - 1 and heights[r + 1] >= cur_height:
                r += 1

            area = (r - l + 1) * cur_height
            ans = max(ans, area)

        return ans

