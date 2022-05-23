nums = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums):
        nums.sort()
        answer=set()
        # Two Pointer 
          
        
        for i in range(len(nums)):
            # nums[i]+(num[j]+nums[k])=0
            # nums[j]+nums[k]=-nums[i]
            # summed=-target
            
            target=-nums[i]
            start=i+1
            end=len(nums)-1
            while start<end:
                summed=nums[start]+nums[end]
                if summed<target:
                    start+=1
                elif summed>target:
                    end-=1
                else:
                    answer.add((nums[i],nums[start],nums[end]))
                    start+=1
                    end-=1
        return answer
x=Solution()
print(x.threeSum(nums))