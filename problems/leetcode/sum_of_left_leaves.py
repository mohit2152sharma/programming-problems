# https://leetcode.com/problems/sum-of-left-leaves/description/?envType=daily-question&envId=2024-04-14
from typing import Optional

from utils.leetcode_tester import TestLeetCode


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def sum_leaves(r, s: int = 0) -> int:

            if r.left or r.right:
                s = sum_leaves(r.left, s)

                if r.right.left:
                    s += sum_leaves(r.right.left, s)
                return s
            else:
                return r.val

        return sum_leaves(root)
