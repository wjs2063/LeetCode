# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        valid=False
        def dfs(root,val):
            nonlocal valid
            if root==None:
                return 
            val+=root.val
            if val==targetSum and root.left==None and root.right==None:
                valid=True
                return
            dfs(root.left,val)
            dfs(root.right,val)
        dfs(root,0)
        return valid