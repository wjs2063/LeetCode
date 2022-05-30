# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid=True
        l=float('-inf')
        r=float('inf')
        def dfs(root,l,r):
            nonlocal valid

            if root==None:
                return
            if l>=root.val or root.val>=r:
                valid=False
                return
            # lower bound upper bound
            dfs(root.left,l,root.val)
            dfs(root.right,root.val,r)
        dfs(root,l,r)
        return valid
                
            