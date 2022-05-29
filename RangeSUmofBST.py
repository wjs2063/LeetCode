# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        val=0
        def recur(root):
            nonlocal val
            if root==None:
                return
            if root.val<low:
                recur(root.right)
            elif low<=root.val<=high:
                val+=root.val
                recur(root.left)
                recur(root.right)
            else:
                recur(root.left)
        recur(root)
        return val