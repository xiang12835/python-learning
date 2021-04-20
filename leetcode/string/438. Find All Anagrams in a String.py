class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lenP = len(p)
        lenS = len(s)
        target = "".join(sorted(p))
        r = []
        for i in range(lenS - lenP + 1):
            if "".join(sorted(s[i:i + lenP])) == target:
                r.append(i)

        return r


class Solution1(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lenP = len(p)
        lenS = len(s)
        target = sorted(p)
        r = []
        for i in range(lenS - lenP + 1):
            if sorted(s[i:i + lenP]) == target:
                r.append(i)

        return r
