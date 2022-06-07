class Solution:
    def mySqrt(self, x: int) -> int:
        def bs(left,right,target):
            mid=(left+right)//2
            if (mid-1)**2<=target<mid**2:
                return mid-1
            elif target<mid**2:
                return bs(left,mid-1,target)
            else:
                return bs(mid+1,right,target)
        return bs(0,2**16,x)
                