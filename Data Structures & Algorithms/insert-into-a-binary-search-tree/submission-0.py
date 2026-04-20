# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val=val)

        if root is None:
            return newNode

        def dfs(node: Optional[TreeNode]):
            if val <= node.val:
                if node.left is None:
                    node.left = newNode
                else:
                    dfs(node.left)

            if val > node.val:
                if node.right is None:
                    node.right = newNode
                else:
                    dfs(node.right)

            return root

        return dfs(root)