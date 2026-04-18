# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def dfs(tree: Optional[TreeNode]) -> int: # calculate height for every node(tree)
            if tree is None:
                return 0

            left_height = dfs(tree.left)
            right_height = dfs(tree.right)

            return 1 + max(left_height, right_height)

        left = dfs(root.left) # get max height of left child
        right = dfs(root.right) # get max height of right child

        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
