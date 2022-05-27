from bisect import bisect_left,bisect_right 
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l=bisect_left(nums,target)
        r=bisect_right(nums,target)
        return [x for x in range(l,r)]
