class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left, right = k, k
        answer = nums[k]
        min_height = nums[k]
        n = len(nums)
        while left > 0 or right < n - 1 :
            if (nums[left - 1] if left else 0 )< (nums[right + 1] if right + 1 < n else 0):
                right += 1
            else:
                left -= 1
            min_height =  min(min_height,nums[left],nums[right])
            answer = max(min_height * (right - left + 1),answer)
        return answer
    
    # Time space O(N), Space O(1)
            