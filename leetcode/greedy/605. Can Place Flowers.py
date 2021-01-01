# coding=utf-8

"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        简单地使用贪心的思路，能够种花就种，不能种就往后继续尝试，直到所有格子都试过为止。
        """
        length = len(flowerbed)
        for i in range(length):
            # 如果已经种够花了，可以提前返回true
            if n <= 0:
                return True

            # 如果已经种过花了，则不能再种了
            if flowerbed[i] == 1:
                continue

            # 如果上一个格子已经种过花了，则当前这格不能种花
            if i > 0 and flowerbed[i - 1] == 1:
                continue

            # 如果下一个格子已经种过花了，则当前这格不能种花
            if i < length - 1 and flowerbed[i + 1] == 1:
                continue

            # 可以种花了，并且记录次数
            flowerbed[i] = 1
            n -= 1

        return n <= 0
