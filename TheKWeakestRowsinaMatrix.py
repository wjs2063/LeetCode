class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s=[]
        i=0
        for matrix in mat:
            s.append((i,sum(matrix)))
            i+=1
        s.sort(key=lambda x:x[1])
        answer=[]
        for s1,s2 in s:
            answer.append(s1)
        return answer[:k]
        