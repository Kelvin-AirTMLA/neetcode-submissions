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

        current = root
        return max_depth + max(self.maxDepth(current.left), self.maxDepth(current.right))