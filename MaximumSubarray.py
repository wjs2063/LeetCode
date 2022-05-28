class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        #흠...간단한데 이걸 생각하기 되게 어려움
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)