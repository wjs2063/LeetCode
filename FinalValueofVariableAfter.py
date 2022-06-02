from collections import defaultdict
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d=defaultdict(int)
        
        for e in operations:
            d[e]+=1
        answer=0        
        for types in d.keys():
            if types in ['--X','X--']:
                answer-=d[types]
            else:
                answer+=d[types]
        return answer