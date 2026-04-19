# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_traversal = list()

        if root is None:
            return []

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            
            left = dfs(node.left)
            inorder_traversal.append(node.val)
            right = dfs(node.right)

            return inorder_traversal

        return dfs(root)
        
