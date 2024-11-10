"""Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'`, determine if the input string is valid

An input string is valide if
    
    1. Open brackets must be closed by the same type of brackets
    2. Open brackets must be closed in the correct order
    3. Every close bracket has a corresponding open bracket of the same type.
"""

from utils.leetcode_tester import TestLeetCode


class Solution:
    def isValid(self, s: str) -> bool:

        open = ["(", "{", "["]
        close = [")", "}", "]"]

        length = len(s)
        if length % 2 != 0:
            return False

        stack = []
        for char in s:
            if char in open:
                stack.append(char)
            elif char in close:
                close_index = close.index(char)
                if len(stack) > 0 and open[close_index] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":

    test_cases = ["()", "()[]{}", "(]", "([)]"]

    tester = TestLeetCode(
        test_cases=test_cases,
        solution=Solution().isValid,
        expected_output=[True, True, False, False],
    )
    tester.check_results()
