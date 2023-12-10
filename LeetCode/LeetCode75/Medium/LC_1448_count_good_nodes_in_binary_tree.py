# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # items in the stack are [node, maximum value up to that node]
        stack = [[root, root.val]]
        good_nodes = 0
        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                good_nodes += 1
            if node.left is not None:
                new_max = max(max_val, node.left.val)
                stack.append([node.left, new_max])
            if node.right is not None:
                new_max = max(max_val, node.right.val)
                stack.append([node.right, new_max])
        return good_nodes
