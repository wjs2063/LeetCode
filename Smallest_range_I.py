class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        mini = min(nums)
        
        if maxi - mini -2*k <= 0 :
            return 0
        else:
            return maxi - mini -2*k
    # Time : O(N), Space : O(1)
    # a - k <= maxi <= a + k
    # b - k <= mini <= b + k 
    # a - b - 2k <= maxi - mini <= a - b + 2k
    # a - b - 2k <= 0 -> 0 , else itself