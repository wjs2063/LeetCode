class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0]*(len(arr))
        prefix[0]=arr[0]
        for i in range(1,len(arr)):
            prefix[i]=prefix[i-1]^arr[i]
        answer=[]
        for x,y in queries:
            if x==0:
                result=prefix[y]
                answer.append(result)
            else:
                result=prefix[x-1]^prefix[y]
                answer.append(result)
        return answer
            