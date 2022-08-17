class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        path = set(nums)
        for i in range(2**n):
            
            x = bin(i)[2:].zfill(n)
            if x not in path:
                return x
        
        return -1