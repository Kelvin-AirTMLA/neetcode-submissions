# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True


        def dfs(n1, n2):
            if n1 is None and n2 is None:
                return True

            if n1 is None or n2 is None:
                return False

            if n1.val != n2.val:
                return False

            return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)

        return dfs(p, q)
