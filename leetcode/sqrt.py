"""Given a non-negative integer `x`, compute and return the square of `x` without using inbuilt function like `pow`"""

from utils.leetcode_tester import TestLeetCode


class Solution:
    def mySqrt(self, x: int) -> int:

        starter = 1
        epsilon = 1

        while epsilon > 0.00005:
            root = 0.5 * (starter + x / starter)
            epsilon = abs(root - starter)
            starter = root

        return int(root) #type: ignore


if __name__ == "__main__":

    tester = TestLeetCode(
        test_cases=[0, 2, 4, 8, 9],
        solution=Solution().mySqrt,
        expected_output=[0, 1, 2, 2, 3],
    )
    tester.check_results()
