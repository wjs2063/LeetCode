from collections import defaultdict
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        h=defaultdict(int)
        for n in range(lowLimit,highLimit+1):
            digit=0
            for x in str(n):
                digit+=int(x)
            h[digit]+=1
        return max(h.values())
        # T:worst(O(N logM)):= O(N*logM) , S:O(1)
        # N번반복은 당연하고 자리숫자만큼 반복할텐데 상용로그값->log n --> 자리숫자와관련
        #최대 공간 1<=x<=100000
        # 즉 99999일때 -> 합 45로 
        # list 의 길이는 최대 45임