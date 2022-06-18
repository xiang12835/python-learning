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

class Solution4:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        法三：快排思想 + 原地

        如果是 (0, 1)，那么万事大吉 i++ 并且 j--。
        如果是 (1, 0)，那么交换两个元素，然后继续。
        如果是 (0, 0)，那么说明 i 位置是正确的，只能 i++。
        如果是 (1, 1)，那么说明 j 位置是正确的，只能 j--。

        T: O(N)
        S: O(1)
        """

        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] % 2 == 1 and nums[r] % 2 == 0: # (1,0)
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] % 2 == 0 and nums[r] % 2 == 1:
                l += 1
                r -= 1
            elif nums[l] % 2 == 0 and nums[r] % 2 == 0:
                l += 1
            elif nums[l] % 2 == 1 and nums[r] % 2 == 1:
                r -= 1

        return nums


class Solution5:
    def sortArrayByParity(self, nums):
        """

        法四：快排思想 + 原地

        如果是 (0, 1)，那么万事大吉 i++ 并且 j--。
        如果是 (1, 0)，那么交换两个元素，然后继续，i++ 并且 j--。
        如果是 (0, 0)，那么说明 i 位置是正确的，只能 i++。
        如果是 (1, 1)，那么说明 j 位置是正确的，只能 j--。

        T: O(N)
        S: O(1)
        """

        l = 0
        r = len(nums) - 1
        while l < r:
            # (1,0)
            if nums[l] % 2  == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            # (0,1)
            elif nums[l] % 2  == 0 and nums[r] % 2 == 1:
                l += 1
                r -= 1
            # (0,0)
            elif nums[l] % 2  == 0 and nums[r] % 2 == 0:
                l += 1
            # (1,1)
            elif nums[l] % 2  == 1 and nums[r] % 2 == 1:
                r -= 1

        return nums


class Solution6(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        法三：双指针 + 一次遍历

        如果左指针指向的是偶数，不操作，左指针向后移动一位。
        如果右指针指向的是奇数，不操作，右指针向前移动一位。
        只有当左指针向奇数，右指针指向偶数时，交换位置，并且左指针向后移、右指针向前移。

        """

        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2 == 1:
                r -= 1
            elif nums[l] % 2 > nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return nums


class Solution7:
    def sortArrayByParity(self, nums):
        """

        法三：双指针+一次遍历

        如果左指针指向的是偶数，不操作，左指针向后移动一位。
        如果右指针指向的是奇数，不操作，右指针向前移动一位。
        只有当左指针向奇数，右指针指向偶数时，交换位置，并且左指针向后移、右指针向前移。

        """

        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 0:
                l += 1
            while l < r and nums[r] % 2 == 1:
                r -= 1
            if nums[l] % 2 > nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return nums
