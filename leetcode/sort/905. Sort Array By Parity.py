class Solution1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        法一：排序
        T: O(NlogN)
        S: O(N)
        """
        return sorted(nums, key=lambda x:x%2)


class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        法二：遍历
        T: O(N)
        S: O(N)
        """
        return [num for num in nums if num % 2 == 0] + [num for num in nums if num % 2 == 1]


class Solution3:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        法三：快排思想 + 原地

        T: O(N)
        S: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2: # (1, 0)
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] % 2 == 0: # (0, 1) or (0, 0)
                left += 1

            if nums[right] % 2 == 1: # (1, 0)
                right -= 1

        return nums
