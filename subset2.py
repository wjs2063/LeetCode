class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = set()
        nums.sort()
        def backtrack(j, sub ):
            for i in range(j, len(nums)):
                if i > j and nums[i - 1] == nums[i]:
                    continue
                backtrack(i + 1, sub + [nums[i]])
            x = tuple(sub)
            if x not in path:
                answer.append(sub)
                path.add(x)
        
        answer = []
        
        backtrack(0,[])
        
        return answer
        
        