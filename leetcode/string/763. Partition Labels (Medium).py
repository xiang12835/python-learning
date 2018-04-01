# coding=utf-8

"""
 A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.

"""


# Time:  O(n)
# Space: O(n)

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lookup = {c: i for i, c in enumerate(S)}
        first, last = 0, 0
        result = []
        for i, c in enumerate(S):
            last = max(last, lookup[c])
            if i == last:
                result.append(i-first+1)
                first = i+1
        return result


if __name__ == "__main__":
    s = Solution()
    print s.partitionLabels("ababcbacadefegdehijhklij")