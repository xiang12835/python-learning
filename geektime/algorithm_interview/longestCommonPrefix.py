# coding=utf-8

"""

5、编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        r = ""

        for data in zip(*strs):
            ss = set(data)
            if len(ss) == 1:
                r += ss.pop()  # Set pop() 方法用于随机移除一个元素。
            else:
                break

        return r