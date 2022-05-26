# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        answer=0
        def summation(root):
            nonlocal answer
            x=0
            if root==None:
                return 0
            l=root.left
            r=root.right
            summation(root.left)
            summation(root.right)
            if root.val%2==0:
                if l:
                    if l.left:
                        x+=l.left.val
                    if l.right:
                        x+=l.right.val
                if r:
                    if r.left:
                        x+=r.left.val
                    if r.right:
                        x+=r.right.val
                answer+=x
        summation(root)
        return answer