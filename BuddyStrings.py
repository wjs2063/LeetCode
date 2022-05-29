class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # not same length False
        if len(s)!=len(goal):
            return False
        # if same length then check
        if s==goal:
            if len(s)-len(set(s))>=1:
                # there is repeated alphabet
                return True
            else:
                # there is not repeated alphabet
                return False
        
        
        a,b=[],[]
        
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            if s[i]!=goal[i]:
                a.append(s[i])
                b.append(goal[i])
        # swapping is only one chance
        
        if len(a)==len(b)==2:
            if set(a)==set(b):
                return True
            else:
                return False
        else:
            return False