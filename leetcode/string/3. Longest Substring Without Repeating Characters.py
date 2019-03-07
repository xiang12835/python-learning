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
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        slow, fast = 0, 0
        res, lookup = 0, set()
        while slow < len(s) and fast < len(s):
            if s[fast] not in lookup:
                lookup.add(s[fast])
                res = max(res, fast - slow + 1)
                fast += 1
            else:
                lookup.discard(s[slow])
                slow += 1
        return res




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
            if lookup[s[fast]] == 1:
                counter += 1
            fast += 1
            # counter < fast - slow 说明有重复字符出现，正常为counter == fast - slow
            while slow < fast and counter < fast - slow:
                lookup[s[slow]] -= 1
                if lookup[s[slow]] == 0:
                    counter -= 1
                slow += 1
            res = max(res, fast - slow)
        return res


if __name__ == '__main__':
    s = "abcabcbb"
    r = Solution().lengthOfLongestSubstring(s)
    print r


