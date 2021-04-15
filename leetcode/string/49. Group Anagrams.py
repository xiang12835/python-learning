# coding=utf-8

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        排序 + 哈希

        时间复杂度：O(nklogk)
        空间复杂度：O(nk)
        """
        d = {}
        for ss in strs:
            key = ''.join(sorted(ss))
            if key in d:
                d[key].append(ss)
            else:
                d[key] = [ss]
        return list(d.values())
