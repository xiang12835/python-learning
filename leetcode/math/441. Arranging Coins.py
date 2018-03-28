# coding=utf-8


"""

你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.

示例 2:

n = 8

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

因为第四行不完整，所以返回3.


"""


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 1
        s = 1
        while s <= n:
            row += 1
            s += row

        return row - 1


class Solution1(object):
    def arrangeCoins(self, n):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, n
        while l <= r:
            mid = (l + r) / 2
            s = mid * (mid + 1) / 2
            if n == s:
                return mid
            elif n > s:
                l = mid + 1
            else:
                r = mid - 1

        return r


if __name__ == "__main__":
    s = Solution()
    print s.arrangeCoins(5)

    s1 = Solution1()
    print s1.arrangeCoins(5)
