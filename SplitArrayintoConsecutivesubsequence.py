from collections import defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        #count_nums: nums 에있는 숫자들을 counting
        #end_array[i]: i로끝나는 배열의 개수 
        count_nums=defaultdict(int)
        end_array=defaultdict(int)
        for i in nums:
            count_nums[i]+=1
        for x in nums:
            if count_nums[x]==0:
                continue
            count_nums[x]-=1
            # x-1로 끝나는 배열이 존재하면
            elif end_array[x-1]>0:
                # x-1로 끝나는 배열을 하나줄이고
                end_array[x-1]-=1
                #x로끝나는배열을 하나늘린다
                end_array[x]+=1
                # 숫자도 하나줄인다
            #만약 x-1로 끝나는 배열이 존재하지않는다면
            # 마지막으로 x x+1 x+2 존재여부
            elif count_nums[x+1]>0 and count_nums[x+2]>0:
                end_array[x+2]+=1
                count_nums[x+1]-=1
                count_nums[x+2]-=1
            else:
                return False
        return True
            