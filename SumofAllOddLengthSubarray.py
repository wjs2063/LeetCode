class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum=[]
        sum_val=0
        for num in arr:
            sum_val+=num
            prefix_sum.append(sum_val)
        s=0
        for i in range(1,len(arr)+1,2):
            j=0
            while i+j<len(arr)+1:
                s+=sum(arr[j:j+i])
                j+=1
        return s
                
            