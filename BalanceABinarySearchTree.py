# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        val=[]
        def inorder(root):
            if root:
                inorder(root.left)
                val.append(root.val)
                inorder(root.right)
        # ascending array val
        inorder(root)
        # now val is not empty
        
        def tree(arr):
            if not arr:
                return None
            l=len(arr)//2
            root=TreeNode(arr[l])
            root.left=tree(arr[:l])
            root.right=tree(arr[l+1:])
            return root
        return tree(val)