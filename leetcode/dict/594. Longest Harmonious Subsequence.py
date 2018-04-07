import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        d = collections.Counter(nums)
        for num in nums:
            if num + 1 in d:
                r = max(r, d[num] + d[num + 1])
        return r


if __name__ == "__main__":
    s = Solution()
    print s.findLHS([1,3,2,2,5,2,3,7])
