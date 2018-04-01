"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
"""


# Time:  O(n^2)
# Space: O(n)
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda (h, k): (-h, k))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result


if __name__ == "__main__":
    s = Solution()
    print s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
