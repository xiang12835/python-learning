class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        if needle == "":
            return 0

        haystack_length = len(haystack)
        needle_length = len(needle)
        for i in xrange(haystack_length):
            if haystack[i:i + needle_length] == needle:
                return i
