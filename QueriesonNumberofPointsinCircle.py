class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        #각 queries[j]번째 원안에있는 points 원소들의 개수찾기
        answer=[]
        for center_x,center_y,radius in queries:
            count=0
            for x,y in points:
                if (x-center_x)**2+(y-center_y)**2<=radius**2:
                    count+=1
            answer.append(count)
        return answer
                