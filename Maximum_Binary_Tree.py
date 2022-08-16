# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(nums):
            if len(nums) < 1 :
                return
            maxi = max(nums)
            index = nums.index(maxi)
            
            node = TreeNode(maxi)
            
            node.left = dfs(nums[:index])
            node.right = dfs(nums[index+1:])
            
            return node
        return dfs(nums)