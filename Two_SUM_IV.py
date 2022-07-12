# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        element=[]
        def dfs(root):
            if root==None:
                return
            dfs(root.left)
            element.append(root.val)
            dfs(root.right)
        dfs(root)
        l,r=0,len(element)-1
        while l<r:
            if element[l]+element[r]==k:
                return True
            elif element[l]+element[r]<k:
                l+=1
            else:
                r-=1
        return False
        # Time O(2N)->O(N) space O(N)
                