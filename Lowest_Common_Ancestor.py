# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root,p,q):
            # 원하는 노드를 찾으면 리턴
            if root == None or root == p or root == q:
                return root
            
            
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)
            # 만약 둘다 존재하면 현재 root 가 최소조상노드
            if left and right:
                return root
            return left if left else right
    
        answer = dfs(root,p,q)
        return answer