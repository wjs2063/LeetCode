class Solution:
    def bitwiseComplement(self, n: int) -> int:
        answer='0b'
        for x in format(n,'b'):
            if x=='1':
                answer+='0'
            else:
                answer+='1'
        return int(answer,2)
        # T: O(log_2(n)), space: O(log_2(n))
            
        