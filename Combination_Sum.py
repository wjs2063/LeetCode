class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        path = set()
        def dfs(arr,s,path,cnt):
            if s > target:
                return
            if s == target and tuple(arr) not in path:
                answer.append(arr)
                path |= {tuple(arr)}
                return 
            for i in range(cnt,len(candidates)):
                dfs(arr+[candidates[i]],s+candidates[i] ,path,i)
        dfs([],0,path,0)
        return answer