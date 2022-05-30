class Solution:
    def reverseWords(self, s: str) -> str:
        string=s.split(" ")
        s=[]
        for x in string[::-1]:
            if x=='':
                continue
            s.append(x)
            
        return " ".join(s)
        