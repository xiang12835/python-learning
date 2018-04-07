"""
 Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length = len(temperatures)
        r = []
        for i in range(length):
            count = 0

            for j in range(i + 1, length):
                count += 1
                if temperatures[j] > temperatures[i]:
                    break
                if j == length - 1:
                    count = 0

            r.append(count)

        return r


if __name__ == "__main__":
    s = Solution()
    print s.dailyTemperatures([4,5,2,3,1])
