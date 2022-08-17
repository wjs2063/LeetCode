# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            
            if root == None :
                return None
            # 왼쪽자식과 오른쪽자식에 dfs 똑같이 적용
            # 해당함수는 먼저 쭉 ! 분기한후에 거꾸로 돌아오는방식으로 동작 될것
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            # left,child 가 다 없고 root.val 이 0이면 None 으로 바꿔주자
            # 해당방식 꿀팁 : 일단은 재귀로 작성후에 마지막 끝에다다랐을때 어떻게 적용시킬것인가를 적어주면됨
            if not root.left and not root.right and not root.val :
                return None
            return root
        root = dfs(root)
        return root