class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        dp=[0]*(n+1)
        dp[0],dp[1]=0,1
        i=1
        while 2*i+1<=n:
            dp[2*i]=dp[i]
            dp[2*i+1]=dp[i]+dp[i+1]
            i+=1
        return max(dp)