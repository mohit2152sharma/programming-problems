# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
from utils.leetcode_tester import TestLeetCode


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])


if __name__ == "__main__":

    tester = TestLeetCode(
        test_cases=["the sky is blue", "blue is sky the"],
        solution=[Solution().reverseWords],
        expected_output=["blue is sky the", "the sky is blue"],
    )
    tester.check_results()
