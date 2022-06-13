# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=1,n
        answer=0
        while l<=r:
            mid=(l+r)//2
            if isBadVersion(mid):
                answer=mid
                r=mid-1
                continue
            l=mid+1
        #bad version is always exist?
        return answer
        