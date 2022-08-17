class Solution:
    def countArrangement(self, n: int) -> int:
        
        
        num = [i for i in range(1,n + 1)]
        table = defaultdict(int)
        for x in num:
            table[x] += 1
        answer = 0
        def dfs(perm,cnt):
            nonlocal answer
            if cnt >= n :
                answer += 1
                return
            for i in range(n):
                if table[num[i]] == 0:
                    continue
                table[num[i]] -= 1
                if  num[i] % (cnt + 1)  == 0 or (cnt + 1) % num[i] == 0:
                    dfs(perm+[num[i]],cnt + 1)
                table[num[i]] += 1
                
        dfs([],0)
        return answer
                