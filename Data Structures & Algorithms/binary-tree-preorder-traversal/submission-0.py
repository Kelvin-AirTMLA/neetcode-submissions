# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        preorder_traversal = list()

        def dfs(node):
            if node is None:
                return

            preorder_traversal.append(node.val)
            left = dfs(node.left)
            right = dfs(node.right)

            return preorder_traversal

        return dfs(root)
