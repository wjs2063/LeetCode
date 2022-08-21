class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cnt = 0 
        now_capacity = capacity
        
        for i in range(len(plants)):
            if plants[i] <= now_capacity :
                cnt += 1
                now_capacity -= plants[i]
            else:
                cnt += 2*i + 1
                now_capacity = capacity - plants[i]
        return cnt