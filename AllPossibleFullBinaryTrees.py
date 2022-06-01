# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp=[[] for _ in range(n+1)]
        dp[1]=[TreeNode()]
        #explain= ( Root):1 Left(1,3,5, . . .) and Right(1,3,5, . . .)
        #so N,Left,Right is always odd number (홀수여야함)
        #that is Left + Right=N-1  
        
        #dp[x]: possible case with x nodes
        
        # i in total node (because dp bottom-up)
        for i in range(1,n+1,2):
            # j is left or right
            for j in range(1,i,2):
                for lefttree in dp[j]:
                    # because Left+right=i-1 -> right=i-left-1
                    for righttree in dp[i-j-1]:
                        dp[i].append(TreeNode(0,lefttree,righttree))
        return dp[n]