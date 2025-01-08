# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], targetSum: int, subTotal: int, include: bool) -> int:
        if root is None:
            return 0
            
        count = 0
        subTotal = subTotal + root.val
        if subTotal == targetSum:
            count += 1
        
        count += self.dfs(root.left, targetSum, subTotal, True) + self.dfs(root.right, targetSum, subTotal, True)
        if not include:
            count += self.dfs(root.left, targetSum, 0, False) + self.dfs(root.right, targetSum, 0, False)

        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = self.dfs(root, targetSum, 0, False)
        return cnt 
        