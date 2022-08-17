class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def dfs(arr,cnt,k):
            nonlocal answer
            if cnt > n + 1 :
                return
            if len(arr) == k:
                answer.append(arr)
            for i in range(cnt,n + 1):
                dfs(arr+[i],i+1,k)
        dfs([],1,k)
        return answer