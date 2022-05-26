class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        INF=float("inf")
        dp=[0]*(n+1)
        for i in range(2,n+1):
            #2칸 or 1칸
            dp[i]=min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        return dp[n]
        