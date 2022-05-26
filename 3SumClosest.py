from collections import deque
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #sort
        nums.sort()
        prev_sum=sum(nums[:3])
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                now_sum=nums[l]+nums[r]+nums[i]
                # 차이가 적은것을 갱신
                if abs(now_sum-target)<abs(prev_sum-target):
                    prev_sum=now_sum
                #sorting 되었다는 전제하에 now_sum이 target보다작으면 left를 증가
                if now_sum<target:
                    l+=1
                # target보다 크면 right을 감소 
                else:
                    r-=1
        return prev_sum
                
            
