"""
 Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:

Input: "UD"
Output: true

Example 2:

Input: "LL"
Output: false

"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")



import collections


class Solution1(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = collections.Counter(moves)
        return d.get("U") == d.get("D") and d.get("L") == d.get("R")


if __name__ == "__main__":
    s = Solution()
    print s.judgeCircle("UD")

    s1 = Solution1()
    print s1.judgeCircle("UD")
