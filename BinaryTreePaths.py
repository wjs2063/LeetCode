# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer=[]
        path=[]
        def dfs(root):
            if root==None:
                return
            path.append(str(root.val))
            # if leaf node
            if root.left==None and root.right==None:
                answer.append("->".join(path))
            #left, right dfs
            dfs(root.left)
            dfs(root.right)
            # end then pop
            path.pop()
        dfs(root)
        return answer