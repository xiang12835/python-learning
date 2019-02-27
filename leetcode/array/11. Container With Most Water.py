# coding=utf-8

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        左右对撞
        """

        left, right = 0, len(height) - 1

        most_water = 0
        while left <= right:
            water = (right - left) * min(height[left], height[right])
            most_water = max(most_water, water)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return most_water
