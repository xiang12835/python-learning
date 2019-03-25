# coding=utf-8

"""

4、给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在 坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的 两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明:你不能倾斜容器，且 n 的值至少为 2。


Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.


"""

class Solution(object):
    def maxArea(self, height_list):
        # 左右对撞

        left = 0
        right = len(height_list) - 1

        most_water = 0
        while left < right:
            water = (right - left) * min(height_list[left], height_list[right])
            most_water = max(most_water, water)

            if height_list[left] < height_list[right]:
                left += 1
            elif height_list[left] > height_list[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return most_water
