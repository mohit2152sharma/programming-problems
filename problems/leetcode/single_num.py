from typing import List

from utils.leetcode_tester import TestLeetCode

"""Given a non empty array of numbers, every element appears twice, except for one. Find that single one."""
"""Solution has time complexity of at max 2n and space complexity of # of unique elements in nums"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        element_count = {}
        for num in nums:
            if num in element_count:
                element_count[num] += 1
            else:
                element_count[num] = 1

        for key, value in element_count.items():
            if value == 1:
                return key


if __name__ == "__main__":

    tester = TestLeetCode(
        test_cases=[[1, 2, 2, 3, 3, 4], [3, 2, 2], [4, 4, 4, 5]],
        solution=Solution().singleNumber,
        expected_output=[1, 3, 5],
    )
    tester.check_results()
