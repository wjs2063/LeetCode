class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp=[[0]*(6) for _ in range(n+1)]
        
        dp[1][5],dp[1][4],dp[1][3],dp[1][2],dp[1][1]=1,1,1,1,1
        # 5='a' 4='e' 3='i' 2='o' 1='u' mapping
        # then assumptuion n=3 then start with a or e or i or u
        # a [all case when n=2 ] e[all case when 2 with out start with a]
        # 점화식 -> DP[n][5]=dp[n-1][5]+[4]+[3]+[2]+[1]
        # -> Dp[n][4]=Dp[n-1][4]+[3]+[2]+[1] 
        for i in range(2,n+1):
            for j in range(1,5+1):
                dp[i][j]=sum(dp[i-1][:j+1])
        return sum(dp[n][:])