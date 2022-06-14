class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        right=max(time)*totalTrips
        left=0
        answer=float('inf')
        while left<=right:
            s=0
            mid=(left+right)//2
            for t in time:
                s+=mid//t
            #middle 시간내에 갈수있는 s is totaltrip
            if s>=totalTrips:
                answer=min(answer,mid)
                right=mid-1
            #시간을늘려야함
            else:
                left=mid+1
            print(s,mid,left,right,answer)
        return answer