# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        passed_val=[]
        queue=deque([])
        queue.append((root,[root.val]))
        cnt=0
        while queue:
            x,passed=queue.popleft()
            if x.left:
                queue.append((x.left,passed+[x.left.val]))
            if x.right:
                queue.append((x.right,passed+[x.right.val]))
            if x.val>=max(passed):
                cnt+=1
        return cnt
            