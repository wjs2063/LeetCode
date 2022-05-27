class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def subset(idx=0,summation=0):
            # 종료조건
            if idx==len(nums):
                return summation
            # i-th element 가 포함되어있거나 안되있거나 2^n으로 분기되면서 각경우에맞게 xor연산더해짐
            return subset(idx+1,summation^nums[idx])+subset(idx+1,summation)
        return subset(0,0)