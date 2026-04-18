# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inverted_binary_tree = list()

        if root is None:
            return None
        
        # swap the children of the first 3 noded tree
        tmp = root.right
        root.right = root.left
        root.left = tmp

        # swap the children of the lower left and right 3 noded trees
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
