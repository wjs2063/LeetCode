# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(l,r):
            if l==None and r==None:
                return True
            # 둘중하나가 None 이라면 
            if l==None or r==None:
                return False
            if l.val==r.val:
                print(l.val,r.val)
                return check(l.left,r.right) and check(l.right,r.left)
            return False
        return check(root.left,root.right)
            