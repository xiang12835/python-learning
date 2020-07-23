# coding=utf-8


"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str

        左右指针

        T: O(n)
        S: O(1)
        """
        ss = list(S)
        l = 0
        r = len(S) - 1
        while l < r:
            while l < r and not ss[l].isalpha():
                l += 1
            while l < r and not ss[r].isalpha():
                r -= 1

            ss[l], ss[r] = ss[r], ss[l]
            l += 1
            r -= 1

        return ''.join(ss)