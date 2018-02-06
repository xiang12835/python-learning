class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in digits:
            sum = sum * 10 + i

        return [int(i) for i in str(sum + 1)]


if __name__ == '__main__':
    s = Solution()
    print s.plusOne([3,9])

