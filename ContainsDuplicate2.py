from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        table = defaultdict(list)
        
        for index,item in enumerate(nums) :
            table[item].append(index)
        for key in table.keys():
            for i in range(1,len(table[key])):
                if table[key][i]-table[key][i-1] <= k :
                    return True
        return False

# 각 value 에 해당하는 key 값들을 다모아본다 그리고 비교해봄

from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cash_table = defaultdict( lambda :-10**5 +1)
        for index,num in enumerate(nums) :
            if index - cash_table[num] <= k :
                return True
            else:
                cash_table[num] = index
        return False
        

# 각 value 에 해당하는 key 값들을 다모아본다 그리고 비교해봄