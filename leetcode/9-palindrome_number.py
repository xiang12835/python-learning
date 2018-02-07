'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return int(str(abs(x))[::-1]) == x


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(123)
    print s.isPalindrome(-123)
    print s.isPalindrome(121)
