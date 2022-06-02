class Solution:
    def romanToInt(self, s: str) -> int:
        table={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        i=0
        answer=0
        while i<len(s)-1:
            if table[s[i]]<table[s[i+1]]:
                answer-=table[s[i]]
            else:
                answer+=table[s[i]]
            i+=1
        return answer+table[s[-1]]
            