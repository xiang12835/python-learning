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


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        """
        二分查找

        T: O(logN)
        S: O(1)

        无重复元素
        """
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:                  # 循环不变式，如果left == right，则循环结束
            mid = l + (r-l)//2        # 区间的中间点
            if nums[mid] < nums[r]:   # 明确中值 < 右值，最小值在左半边，收缩右边界
                r = mid               # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处
            elif nums[mid] > nums[r]: # 中值 > 右值，最小值在右半边，收缩左边界
                l = mid + 1           # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
        return nums[l]                # 循环结束，left == right，最小值输出nums[left]或nums[right]均可

if __name__ == "__main__":
    nums = [2,4,5,6,7,0,1]

    s = Solution()
    print(s.findMin(nums))

