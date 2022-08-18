class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # increase or decrease 에 맞게 index,last 에 갱신해주고 계속비교
        def is_monotonic(nums,types):
            if types =='increase':
                index , last = 0,nums[0]
                for i in range(1,len(nums)):
                    if index <= i and last <= nums[i]:
                        index = i
                        last  = nums[i]
                    else:
                        return False
                return True
            if types =='decrease':
                index , last = 0 ,nums[0]
                for i in range(1,len(nums)):
                    if index <= i and last >= nums[i]:
                        index = i
                        last = nums[i]
                    else:
                        return False
                return True
            return -1
        return is_monotonic(nums,'increase') | is_monotonic(nums,'decrease')