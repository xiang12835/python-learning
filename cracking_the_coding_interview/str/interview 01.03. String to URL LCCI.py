# coding=utf-8

"""

Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

Example 1:

Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 2:

Input: "               ", 5
Output: "%20%20%20%20%20"


"""


class Solution(object):
    def replaceSpaces(self, S, length):
        """
        :type S: str
        :type length: int
        :rtype: str
        """
        return S[:length].replace(' ', '%20')

