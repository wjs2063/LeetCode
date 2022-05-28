class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binary_search(arr):
            if arr[-1]>=0:
                return 0
            l=0
            r=len(arr)-1
            while l<r:
                mid=(l+r)//2
                if arr[mid]<0:
                    r=mid
                else:
                    l+=1
            return len(arr[r:])
        s=0
        for arr in grid:
            s+=binary_search(arr)
            
        return s
            