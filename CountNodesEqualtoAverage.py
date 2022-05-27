# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def subtree(root):
            if root==None:
                return 0
            stack=[root]
            cnt=1
            value=0
            while stack:
                top=stack.pop()
                if top.left:
                    stack.append(top.left)
                    cnt+=1
                if top.right:
                    stack.append(top.right)
                    cnt+=1
                value+=top.val
            if root.val==int(value/cnt):
                return 1
            else:
                return 0
        answer=0    
        stack=[root]
        while stack:
            top=stack.pop()
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
            answer+=subtree(top)
        return answer
            