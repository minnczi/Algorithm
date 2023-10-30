from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if root is None:
            return max_depth

        stack = [[root, 1]]
        while stack:
            now, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if now.left is not None:
                stack.append([now.left, depth+1])
            if now.right is not None:
                stack.append([now.right, depth+1])
        return max_depth
