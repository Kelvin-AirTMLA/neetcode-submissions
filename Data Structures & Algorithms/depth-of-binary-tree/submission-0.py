# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 1
        if root is None:
            return 0
        
        left_subtree = self.maxDepth(root.left) # integer depth of left subtree
        right_subtree = self.maxDepth(root.right) # integer depth of right subtree

        return max_depth + max(left_subtree, right_subtree)