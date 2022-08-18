class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        answer = ""
        strs = str(n)
        i = 0
        for index in range(len(strs)-1,-1,-1):
            if i and i % 3 == 0:
                answer += "."
            answer += strs[index]
            i += 1
        return answer[::-1]
# O(log n) , Space : O(log n )