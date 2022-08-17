from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        
        table = defaultdict(int)
        answer = 0 
        
        for num1 in nums1:
            for num2 in nums2:
                total = num1 + num2
                table[total] += 1
        for num3 in nums3:
            for num4 in nums4:
                total = -(num3 + num4)
                if total in table:
                    answer += table[total]
        return answer
                
                        
                    