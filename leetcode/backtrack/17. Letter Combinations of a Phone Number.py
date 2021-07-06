# coding=utf-8

class Solution:
    def letterCombinations(self, digits):
        """
        T：O(3**m×4**n)
        S：O(m+n)
        """
        if not digits:
            return list()

        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combination = []
        res = []

        def backtrack(index):
            if index == len(digits):
                res.append("".join(combination))
            else:
                digit = digits[index]
                for letter in d[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        backtrack(0)
        return res


class Solution1:
    def letterCombinations(self, digits):
        """
        T：O(3**m×4**n)
        S：O(m+n)
        """
        if not digits:
            return list()

        self.d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        self.res = []
        self.backtrack(digits, 0, [])
        return self.res

    def backtrack(self, digits, index, combination):

        # terminator
        if index == len(digits):
            self.res.append("".join(combination))
            return

        digit = digits[index]
        for letter in self.d[digit]:
            # next possibility
            combination.append(letter)

            # drill down
            self.backtrack(digits, index + 1, combination)

            # reverse
            combination.pop()




if __name__ == "__main__":
    print Solution1().letterCombinations("23")