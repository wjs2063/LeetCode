class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
                    
        answer=collections.Counter(arr)
        a=[]
        for key,value in answer.items():
            a.append((value,key))
        a.sort(key=lambda x: x[0])

        answer=set(arr)
        t=0
        for cnt,integer in a:
            if cnt<=k:
                k-=cnt
                t+=1
            else:
                break
        return len(answer)-t