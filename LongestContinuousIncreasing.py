class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l,r=0,0
        answer,cnt=1,1
        #sliding window
        while r<len(nums)-1:
            if nums[r]<nums[r+1]:
                cnt+=1
                answer=max(answer,cnt)
            else:
                cnt=1
            r+=1
        return answer