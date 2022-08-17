from collections import defaultdict
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        table = defaultdict(int)
        maxi = 0 
        n = len(nums)
        def dfs(table,cnt,s ):
            
            nonlocal maxi
            
            maxi = max (maxi, s)
            table[s] += 1
            
            for i in range(cnt,n):
                dfs(table,i + 1,s | nums[i])
        dfs(table,0,0)
        return table[maxi]