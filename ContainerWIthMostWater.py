class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        maximum=0
        
        while left<right:
            temp=(right-left)*min(height[left],height[right])
            
            if temp>maximum:
                maximum=temp
            #left가 더크면 right 을 떙기고
            # right이 더크면 left를 한칸떙기고
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1
        return maximum