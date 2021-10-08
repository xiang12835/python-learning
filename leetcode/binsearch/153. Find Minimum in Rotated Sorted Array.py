# coding=utf-8

class Solution:
    def findMin(self, nums):
        """
        二分查找

        T: O(logN)
        S: O(1)
        """
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        if nums[r] > nums[0]:  # 易错，已经有序
            return nums[0]
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1


if __name__ == "__main__":
    nums = [11, 13, 15, 17]

    s = Solution()
    print(s.findMin(nums))

