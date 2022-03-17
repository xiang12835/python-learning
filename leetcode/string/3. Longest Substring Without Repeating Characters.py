# coding=utf-8

"""

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑动窗口 + 字典

        T: O(N)
        S: O(1)
        """
        if not s:
            return 0

        n = len(s)

        start, end = 0, 0
        r = 0
        lookup = set()

        while start < n and end < n:
            if s[end] not in lookup:
                lookup.add(s[end])
                r = max(r, end - start + 1)
                end += 1
            else:
                lookup.discard(s[start])
                start += 1

        return r

import collections


class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        滑动窗口 + 字典
        """
        d = collections.defaultdict(int)
        end, start, counter, res = 0, 0, 0, 0
        while end < len(s):
            d[s[end]] += 1
            if d[s[end]] == 1: # 唯一
                counter += 1
            end += 1
            # counter < end - start 说明有重复字符出现，正常为counter == end - start
            while start < end and counter < end - start: # 有重复
                d[s[start]] -= 1
                if d[s[start]] == 0:
                    counter -= 1
                start += 1
            res = max(res, end - start)

        return res


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        思路：找出从每一个字符开始的，不包含重复字符的最长子串

        T：O(N)，其中 N 是字符串的长度。左指针和右指针分别会遍历整个字符串一次。
        S：O(∣Σ∣)
        """
        lookup = collections.defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len


if __name__ == '__main__':
    s = "pwwkew"
    r = Solution2().lengthOfLongestSubstring(s)
    print(r)


