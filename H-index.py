from collections import defaultdict
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        # 6 5 3 1 0 (value)
        # 1 2 3 4 5 ( index + 1 ) 
        # index + 1 := value 번 이상 인용된 논문의 개수
        
        citations.sort(reverse = True)
        answer = 0
        for index,value in enumerate(citations):
             
            if value >= index + 1 :
                answer = index + 1 
        return answer
        