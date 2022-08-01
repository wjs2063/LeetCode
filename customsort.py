from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h= defaultdict(lambda:-10)
        for i,c in enumerate(order):
            h[c]=i
        s = list(s)
        # sort based on new order 
        s.sort(key = lambda x: h[x])      
        return ''.join(s) 
