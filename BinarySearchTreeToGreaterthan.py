# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s=0
        def bst(root):
            nonlocal s
            if root==None:
                return
            bst(root.right)
            s+=root.val
            root.val=s
            bst(root.left)
            return s
        bst(root)
        return root