# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75


from itertools import zip_longest

from utils.leetcode_tester import TestLeetCode


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""

        word1_bigger = len(word1) > len(word2)
        first_zip = word1[: len(word2)] if word1_bigger else word1
        second_zip = word2 if word1_bigger else word2[: len(word1)]
        for a, b in zip(first_zip, second_zip):
            ans += a
            ans += b

        if word1_bigger:
            ans += word1[len(word2) :]
        else:
            ans += word2[len(word1) :]

        return ans

    def mergeAlternately2(self, word1: str, word2: str) -> str:

        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))


if __name__ == "__main__":

    tester = TestLeetCode(
        test_cases=[["abc", "pqr"], ["ab", "pqrs"], ["abcd", "pq"]],
        solution=Solution().mergeAlternately2,
        expected_output=["apbqcr", "apbqrs", "apbqcd"],
    )
    tester.check_results()
