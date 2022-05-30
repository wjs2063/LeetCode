# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        answer=float('inf')
        def dfs(root,cnt):
            nonlocal answer
            if root==None:
                return 
            if root==None:
                return 
            #leafnode
            if not root.left and not root.right:
                answer=min(answer,cnt)
                return
            #not leafnode
            else:
                dfs(root.left,cnt+1)
                dfs(root.right,cnt+1)
        dfs(root,1)

        return answer