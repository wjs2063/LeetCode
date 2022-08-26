import heapq


num1 = [30,29,19,5]
num2 = [25,25,25,25,25]
for i in range(len(num2)):
    num2[i]=(-num2[i],i)
heapq.heapify(num2)
stack = []
answer = 0
for i,num in enumerate(num1):
    while num2 and - num2[0][0] >= num :
        stack.append(heapq.heappop(num2))

    if stack and -stack[-1][0] >= num and i <= stack[-1][1]:
        answer = max(answer,stack[-1][1] - i)
    #print(stack,answer,num)
print(answer)


'''
더좋은풀이 
'''


class Solution:
    def maxDistance(self, n1: List[int], n2: List[int]) -> int:
        i = j = res = 0
        while i < len(n1) and j < len(n2):
            if n1[i] > n2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res