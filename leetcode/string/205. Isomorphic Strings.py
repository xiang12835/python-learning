class Solution:
    def isIsomorphic(self, s, t):
        n = len(s)
        for i in range(n):
            if s.index(s[i]) != t.index(t[i]):
                return False

        return True
