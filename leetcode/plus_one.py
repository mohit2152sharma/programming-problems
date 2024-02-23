"""You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""

from typing import List

from utils.leetcode_tester import TestLeetCode


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = int("".join([str(x) for x in digits]))
        num += 1
        return [int(x) for x in str(num)]


if __name__ == "__main__":

    tester = TestLeetCode(
        test_cases=[[1, 2, 3], [9], [1, 2, 9], [4, 9, 9, 9]],
        solution=Solution().plusOne,
        expected_output=[[1, 2, 4], [1, 0], [1, 3, 0], [5, 0, 0, 0]],
    )
    tester.check_results()
