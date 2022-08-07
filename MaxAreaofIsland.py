from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        
        visited=[[False]*(m) for _ in range(n)]
        
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        answer=0
        def bfs(x,y):
            area=0
            nonlocal dx
            nonlocal dy
            nonlocal answer
            q=deque([(x,y)])
            while q:
                x,y=q.popleft()

                if not visited[x][y]:
                    visited[x][y]=True
                    grid[x][y]=0
                    area+=1
                    for i in range(4):
                        nx=x+dx[i]
                        ny=y+dy[i]

                        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                            continue
                        if grid[nx][ny] == 1:
                            q.append((nx,ny))
            answer=max(answer,area)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not visited[i][j]:
                    bfs(i,j)
        return answer
        # Time Space : O (NM) Space O(NM)
                    