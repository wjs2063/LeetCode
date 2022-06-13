class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even=[]
        odd=[]
        even_sum=0
        odd_sum=0
        for i in range(len(nums)):
            if i%2==0:
                even_sum+=nums[i]
                even.append(even_sum)
                odd.append(odd_sum)
            else:
                odd_sum+=nums[i]
                odd.append(odd_sum)
                even.append(even_sum)
        if len(nums)==1:
            return 1
        if len(nums)==2:
            return 0
        cnt=0
        if even[-1]-even[0]==odd[-1]:
            cnt+=1
        for i in range(1,len(nums)):
            if even[i-1]+odd[-1]-odd[i]==odd[i-1]+even[-1]-even[i]:
                cnt+=1
        return cnt