# coding=utf-8

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        二分查找

        法1. 暴力：还原-可以用二分查找去还原 O(logN) -> 升序 -> 二分：O(logN)
        法2. 二分查找：a) 单调 b) 边界 c) index

        第一段有序：[l,mid]
        第二段有序：(mid+1, n-1]

        对于数组中有重复元素的情况，二分查找时可能会有 a[l]=a[mid]=a[r]，此时无法判断区间 [l,mid] 和区间 [mid+1,r] 哪个是有序的。对于这种情况，我们只能将当前二分区间的左边界加一，右边界减一，然后在新区间上继续二分查找。

        有重复

        T: O(logN)
        S: O(1)
        """
        if not nums:
            return False

        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return True

            if nums[l] == nums[m] and nums[m] == nums[r]: # 非降序排列
                l += 1
                r -= 1
            elif nums[l] <= nums[m]: # [l,mid]
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # (mid+1, n-1]
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False
