# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(s,t):
            # no trouble!! 
            if s==None and t==None:
                return True
            #둘중하나가 None 이거나 value가다를경우
            if s==None or t==None or s.val!=t.val:
                return False
            # left side and right side same -> tree same
            return is_same(s.left,t.left) and is_same(s.right,t.right)
        def dfs(root):
            #if root node does not exist
            if root==None:
                return False
            #print(root.val,subRoot.val,is_same(root,subRoot))
            if root.val==subRoot.val and is_same(root,subRoot):
                return True
            return dfs(root.left) or dfs(root.right)
        return dfs(root)