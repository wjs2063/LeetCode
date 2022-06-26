class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # i-> 1'th counting j-> 0'th counting
        i,j=0,0
        k=0
        l_0,l_1=0,0
        # l_0 -> 0'th maximun counting, l_1-> 1'th maximum counting
        while k<len(s):
            if s[k]=='1':
                i+=1
                if l_1<i:
                    l_1=i
                j=0
            elif s[k]=='0':
                j+=1
                if l_0<j:
                    l_0=j
                i=0
            k+=1
        return l_1>l_0