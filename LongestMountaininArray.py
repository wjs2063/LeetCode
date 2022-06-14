class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        cur,asc,desc=0,0,0
        for i in range(1,len(arr)):
            # 감소하다가 증가하거나 flat 한 부분이생긴다면 초기화 
            if desc and arr[i-1]<arr[i] or arr[i-1]==arr[i]:asc,desc=0,0
            #증가 True 는 1로 인식
            asc+=arr[i-1]<arr[i]
            #감소  False 는 0으로 인식 
            desc+=arr[i-1]>arr[i]
            # mountain 이라면 증감부분과 감소부분이있어야함
            if asc and desc:cur=max(cur,asc+desc+1)
        return cur