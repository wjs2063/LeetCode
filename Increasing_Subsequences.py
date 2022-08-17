class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        path = set()
        answer = []
        def dfs(arr,cnt):
            nonlocal path
            nonlocal answer
            t = tuple(arr)
            
            if len(arr) > 1 and t not in path:
                answer.append(arr)
                path.add(t)           
                
            for i in range(cnt,n):
                if arr and nums[i] < arr[-1]:
                    continue
                dfs(arr+[nums[i]],i + 1)
        dfs([],0)
        return answer