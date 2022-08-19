class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        answer = []
        
        digits = list(map(str,digits))
        digits = "".join(digits)
        digits = str(int(digits)+1)
        
        
        for d in digits:
            answer.append(int(d))
        return answer