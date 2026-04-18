from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return False

        def isSameTree(current_tree, subTree):
            if current_tree is None and subTree is None:
                return True

            if current_tree is None or subTree is None:
                return False

            if current_tree.val != subTree.val:
                return False
            
            return isSameTree(current_tree.left, subTree.left) and isSameTree(current_tree.right, subTree.right)

        current = root
        if isSameTree(current, subRoot):
            return True

        return self.isSubtree(current.left, subRoot) or self.isSubtree(current.right, subRoot)
