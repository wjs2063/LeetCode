# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        h=[]
        def search_level(root,level):
            level=level
            heapq.heappush(h,(-level,root.val))
            if root.left!=None:
                search_level(root.left,level+1)
            if root.right!=None:
                search_level(root.right,level+1)
        # 각 노드를 돌면서 각노드의 (level,val)를 저장
        search_level(root,1)
        # 최소힙에 넣으면 level 기준으로 정렬 
        maximum=-h[0][0]
        summed=0
        # heap의 원소를 하나씩뽑으면서 최대 level 과 다르면 덧셈멈추고 break
        while h:
            level_x,val=heapq.heappop(h)
            if level_x+maximum!=0:
                break
            summed+=val
        return summed