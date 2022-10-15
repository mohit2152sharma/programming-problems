"""Write a function to find the longest common prefix string amongst an array of strings"""

from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        lens = list(map(len, strs))
        smallest_str = strs[lens.index(min(lens))]
        strs.pop(strs.index(smallest_str))

        all_matches = []
        for i, char in enumerate(smallest_str):
            all_true = []
            for st in strs:
                if char == st[i]:
                    all_true.append(True)
                else:
                    all_true.append(False)

            all_matches.append(all_true)

        indexes = -1 
        for i in list(map(lambda x: all(x), all_matches)):
            if i: 
                indexes += 1
            else:
                break 
        
        if not indexes == -1:
            common_prefix = smallest_str[:indexes+1]
        return common_prefix


if __name__ == "__main__":

    test1 = ["flower", "flow", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["cir", "car"]

    result1 = Solution().longestCommonPrefix(strs=test1)
    result2 = Solution().longestCommonPrefix(strs=test2)
    result3 = Solution().longestCommonPrefix(strs=test3)

    print(f'Result of test1: {result1}. Expected output: "fl"')
    print(f'Result of test2: {result2}. Expected output: ""')
    print(f'Result of test3: {result3}. Expected output: "c"')
