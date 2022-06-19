class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        遍历

        T: O(N)
        S: O(N)
        """
        n = len(nums)
        evenIndex = 0 # 偶数位置
        oddIndex = 1 # 奇数位置

        res = [0] * n

        for num in nums:
            if num % 2 == 1: # 奇数
                res[oddIndex] = num
                oddIndex += 2
            else:
                res[evenIndex] = num
                evenIndex += 2

        return res

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        双指针

        T: O(N)
        S: O(1)
        """

        n = len(nums)

        oddIndex = 1 # 奇数位
        for evenIndex in range(0, n, 2): # 偶数位
            if nums[evenIndex] % 2 == 1: # 为奇数
                # 从奇数位上找偶数
                while nums[oddIndex] % 2:
                    oddIndex += 2
                nums[evenIndex], nums[oddIndex] = nums[oddIndex], nums[evenIndex]
        return nums
