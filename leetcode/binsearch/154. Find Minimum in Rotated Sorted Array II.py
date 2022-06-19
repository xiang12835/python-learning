# coding=utf-8

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        二分查找

        T: O(logN)
        S: O(1)

        有重复元素
        """
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:                  # 循环不变式，如果left == right，则循环结束
            mid = l + (r - l) // 2    # 区间的中间点
            if nums[mid] < nums[r]:   # 明确中值 < 右值，最小值在左半边，收缩右边界
                r = mid               # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处
            elif nums[mid] > nums[r]: # 中值 > 右值，最小值在右半边，收缩左边界
                l = mid + 1           # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            else:
                r = r - 1             # 不能确定 nums[mid] 究竟在最小值的左侧还是右侧

        return nums[l]                # 循环结束，left == right，最小值输出nums[left]或nums[right]均可
