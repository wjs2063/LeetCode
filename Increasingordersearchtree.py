# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        value=[]
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            value.append(root.val)
            inorder(root.right)
        inorder(root)
        r=TreeNode(value[0])
        start=r
        for i in range(1,len(value)):
            r.right=TreeNode(value[i])
            r=r.right
        return start
            