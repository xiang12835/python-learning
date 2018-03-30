"""
 Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: 3
Output: False

"""
import math


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        sq = set()
        count = int(math.sqrt(c))
        # use (count + 1) because first index is 0
        for i in range(count + 1):
            sq.add(i ** 2)

        for n in sq:
            if c - n in sq:
                return True

        return False


class Solution1(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            powsum = l ** 2 + r ** 2
            if powsum == c:
                return True
            elif powsum > c:
                r -= 1
            else:
                l += 1

        return False


if __name__=="__main__":
    s = Solution()
    print s.judgeSquareSum(4)

    s1 = Solution1()
    print s1.judgeSquareSum(4)