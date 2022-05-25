class Solution:
    def divisorGame(self, n: int) -> bool:
        dp=[False]*(n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                # when dp[i-j] must not win because Alice,Bob,Alice,Bob . . .
                # 번갈아가면서 기회를 얻기때문  
                if i%j==0 and not dp[i-j]:
                    dp[i]=True
        return dp[n]
        