# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q=deque([])
        q.append(cloned)
        while q:
            t=q.popleft()
            if t.val==target.val:
                return t
            if t.left :
                q.append(t.left)
            if t.right:
                q.append(t.right)
