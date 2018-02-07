class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        length = len(nums)
        for i in xrange(length):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index, nums[:index]


if __name__ == '__main__':
    s = Solution()
    print s.removeElement([3,2,1,3,3], 3)
