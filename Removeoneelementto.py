class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # exactly one element 
        answer=[]
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                answer.append(i)
        # len(answer)==0 ? strictly increasing
        if len(answer)==0:
            return True
        if len(answer)==1:
            x=answer[0]
            # A0<A1<A2 , ,<Ak>Ak+1<Ak+2
            # we have two choices  remove k-th index or k+1th index 
            # if we remove k-th index check index [k-1]<[k+1] 
            # if we remove k+1 th index check index [k]<[k+2]
            # constraint--> len  
            if x==0 or x==len(nums)-2:
                return True
            elif nums[x-1]<nums[x+1] or nums[x]<nums[x+2]:
                return True
            else:return False
        return False
        # O(n log(n))