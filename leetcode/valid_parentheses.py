"""Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'`, determine if the input string is valid

An input string is valide if
    
    1. Open brackets must be closed by the same type of brackets
    2. Open brackets must be closed in the correct order
    3. Every close bracket has a corresponding open bracket of the same type.
"""

from utils.leetcode_tester import TestLeetCode

#TODO: incomplete solution
class Solution:
    def isValid(self, s: str) -> bool:

        open = ["(", "{", "["]
        close = [")", "}", "]"]

        length = len(s)
        if length % 2 != 0:
            return False
        i = 0

        for i in range(length):
            k = i + 1
            while k <= length:
                for o, c in zip(open, close):
                    if not s[i] == o and s[i + k] == c:
                        return False
                k += 2
        return True


if __name__ == "__main__":

    test_cases = ["()", "()[]{}", "(]"]

    tester = TestLeetCode(
        test_cases=test_cases,
        solution=Solution().isValid,
        expected_output=[True, True, False],
    )
    tester.check_results()
