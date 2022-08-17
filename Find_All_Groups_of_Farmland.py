from collections import deque
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        r, c = len(land),len(land[0])
        visited = [[False]*(c + 1) for _ in range(r + 1)]
        
        def bfs(start:tuple):
            x1,y1 = start
            x2,y2 = start
            
            q = deque([(x1,y1)])
            
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            
            while q:
                x,y = q.popleft()
                if not visited[x][y]:
                    visited[x][y] = True
                    x2 = max(x2,x)
                    y2 = max(y2,y)
                    
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                        if nx < 0 or nx >= r or ny < 0 or ny >= c or land[nx][ny] == 0 or visited[nx][ny]:
                            continue
                        q.append((nx,ny))
            return x1,y1,x2,y2
                    
                    
            
        answer = []  
            
        for i in range(r):
            for j in range(c):
                if land[i][j] == 1 and not visited[i][j]:
                    answer.append(bfs((i,j)))
        return answer