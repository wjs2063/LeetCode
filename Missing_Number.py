class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        # range [0,n] -> all sum -> (n+1)*(n)/2
        s = sum(nums)
        
        return (n+1)*(n)//2 - s
        # 0~n 까지의 합에서 주어진 list의 sum 을 빼면 해당 숫자가나옴