class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #solution: Combination or Backtracking
        answer=[]
        path=[]
        n=len(nums)
        def back(cnt,path):
            
            answer.append(path[:])
            for i in range(cnt,n):
                back(i+1,path+[nums[i]])

        back(0,path)
        return answer