"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = 0
        for digit in digits:
            s = s * 10 + digit

        s += 1
        return [int(i) for i in str(s)]


if __name__ == '__main__':
    s = Solution()
    print s.plusOne([3,9])

