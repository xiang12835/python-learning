# coding=utf-8

"""
 Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [i.lower() for i in s if i.isalnum()]
        return s[::-1] == s


class Solution1(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ss = "".join(c.lower() for c in s if c.isalnum())
        return ss == ss[::-1]


class Solution2(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

        时间复杂度：O(|s|)，其中 |s| 是字符串 ss 的长度。

        空间复杂度：O(1)。

        """
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome("A man, a plan, a canal: Panama")
    print s.isPalindrome("race a car")
