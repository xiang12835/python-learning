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


class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        快慢指针
        """
        lookup = collections.defaultdict(int)
        fast, slow, counter, res = 0, 0, 0, 0
        while fast < len(s):
            lookup[s[fast]] += 1
            if lookup[s[fast]] == 1: # 唯一
                counter += 1
            fast += 1
            # counter < fast - slow 说明有重复字符出现，正常为counter == fast - slow
            while slow < fast and counter < fast - slow: # 有重复
                lookup[s[slow]] -= 1
                if lookup[s[slow]] == 0:
                    counter -= 1
                slow += 1
            res = max(res, fast - slow)
        return res


if __name__ == '__main__':
    s = "pwwkew"
    r = Solution2().lengthOfLongestSubstring(s)
    print(r)


