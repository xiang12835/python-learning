class Solution:
    def isIsomorphic(self, s, t):
        n = len(s)
        for i in range(n):
            if s.index(s[i]) != t.index(t[i]):
                return False

        return True


class Solution1(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for idx, val in enumerate(s):
            d1[val] = d1.get(val, []) + [idx]
        for idx, val in enumerate(t):
            d2[val] = d2.get(val, []) + [idx]

        return sorted(d1.values()) == sorted(d2.values())