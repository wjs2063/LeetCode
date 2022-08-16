class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        table = defaultdict(int)
        for num in nums:
            table[num] += 1
        answer = []
        def dfs(arr):
            if len (arr) == len(nums):
                answer.append(arr)
                return
            for i in range(-10,10+1):
                if table[i] == 0:
                    continue
                table[i] -= 1
                dfs(arr+[i])
                table[i] += 1
        dfs([])
        return answer