class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer=set()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                s1=nums[i]+nums[j]
                l=j+1
                r=len(nums)-1
                while l<r:
                    s2=nums[l]+nums[r]
                    if s1+s2==target:
                        answer.add((nums[i],nums[j],nums[l],nums[r]))
                    if s2<target-s1:
                        l+=1
                    else:
                        r-=1
        return answer
                    