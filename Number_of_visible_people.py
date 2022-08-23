class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = [0] * (len(heights))
        stack  = []
        
        
        for pos,height in enumerate(heights):
            # stack 이 비어있지않고 스택의 최상단이 현재 높이보다 작다면 (다시말해 볼수있는건 여기까지라는소리)
            # 즉 현재 위치의 height 에서 역으로 stack 에서 pop 하면서 추가 
            while stack and heights[stack[-1]] <= height:
                answer[stack.pop()] += 1
            # 역추적한결과 남아있는게있다면 현재 height 보다 크다는 의미이므로 또 추가 
            if stack :
                answer[stack[-1]] += 1
            stack.append(pos)
        return answer