# coding=utf-8

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        found = 0
        num = 0
        while found < n:
            num += 1
            if self.isUgly(num):
                found += 1

        return num

    def isUgly(self, num):
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return True if num == 1 else False

if __name__ == "__main__":
    s = Solution()
    print s.nthUglyNumber(10)
