from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        vote=[0]*(n+1)
        for t1,t2 in trust:
            vote[t1]-=1
            vote[t2]+=1
        for i in range(1,n+1):
            if vote[i]==n-1:
                return i
        return -1
            