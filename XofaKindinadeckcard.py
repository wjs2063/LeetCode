from collections import defaultdict
import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        group=defaultdict(int)
        # counting
        for d in deck:
            group[d]+=1
        # 1->4, 2->6 면 2개씩 분할가능 즉 4와6의 최대공약수가 2이상이여야함 
        # 일반화 시키면 a,b,c,d,e,f, 의 최대공약수가 결국 2이상이여야 한다는 소리
        x=list(group.values())
        t=x[0]
        for i in range(1,len(x)):
            t=math.gcd(t,x[i])
        return t>=2
        