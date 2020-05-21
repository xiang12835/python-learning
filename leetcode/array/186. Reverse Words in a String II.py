# coding=utf-8

"""
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s = ''.join(s)[::-1]
        r = []
        for word in s.split(' '):
            r.append(word[::-1])
        return list(' '.join(r))


if __name__ == "__main__":

    print Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])

