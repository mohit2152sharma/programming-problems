# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75
from collections import Counter

from utils.leetcode_tester import TestLeetCode


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        return len(set(arr)) == len(set(Counter(arr).values()))

    def uniqueOccurrences2(self, arr: list[int]) -> bool:

        # much slower than the first one
        hashmap = {}
        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        for _, value in hashmap.items():
            if len([x for x in hashmap.values() if x == value]) > 1:
                return False
        return True


if __name__ == "__main__":

    tester = TestLeetCode(
        test_cases=[
            [[1, 2, 2, 1, 1, 3]],
            [[1, 2]],
            [[-3, 0, 1, -3, 1, 1, 1, -3, 10, 10]],
        ],
        solution=[Solution().uniqueOccurrences, Solution().uniqueOccurrences2],
        expected_output=[True, False, True],
    )
    tester.check_results()
