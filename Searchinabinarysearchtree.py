# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def _bst(root):
            nonlocal val
            if root==None:
                return None
            if root.val==val:
                return root
            if val<root.val:
                return _bst(root.left)
            else:
                return _bst(root.right)
        return _bst(root)