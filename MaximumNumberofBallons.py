from collections import defaultdict,Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t=Counter(text)
        a,b=float('inf'),float('inf')
        for x in 'ban':
            a=min(t[x],a)
        for x in 'lo':
            b=min(t[x],b)
        cnt=0
        while True:
            a,b=a-1,b-2
            if a<0 or b<0:
                break
            cnt+=1
        return cnt

## T: O(N) SPACE O(N)