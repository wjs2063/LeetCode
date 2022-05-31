# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        heap=[]
        def dfs(root):
            if root==None:
                return
            heapq.heappush(heap,root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        x=heapq.heappop(heap)
        while heap:
            y=heapq.heappop(heap)
            if x!=y:
                return y
        return -1