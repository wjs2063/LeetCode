n=5
class Solution:
    def countBits(self, n):
        dp=[0 for _ in range(n+1)]
        for i in range(n+1):
            if i%2==1:
                dp[i]=dp[i-1]+1
            else:
                dp[i]=dp[i//2]
        return dp
x=Solution()

print(x.countBits(n))