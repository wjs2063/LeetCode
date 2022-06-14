from collections import deque
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        maximum=[[0]*len(grid[0]) for _ in range(len(grid))]
        minimum=[[0]*len(grid[0]) for _ in range(len(grid))]
        
        maximum[0][0]=grid[0][0]
        minimum[0][0]=grid[0][0]
        
        for k in range(1,len(grid[0])):
            maximum[0][k]=maximum[0][k-1]*grid[0][k]
            minimum[0][k]=minimum[0][k-1]*grid[0][k]
        for i in range(1,len(grid)):
            maximum[i][0]=maximum[i-1][0]*grid[i][0]
            minimum[i][0]=minimum[i-1][0]*grid[i][0]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if grid[i][j]>0:
                    maximum[i][j]=max(maximum[i-1][j],maximum[i][j-1])*grid[i][j]
                    minimum[i][j]=min(minimum[i-1][j],minimum[i][j-1])*grid[i][j]
                # if negative 
                else:
                    maximum[i][j]=min(minimum[i-1][j],minimum[i][j-1])*grid[i][j]
                    minimum[i][j]=max(maximum[i-1][j],maximum[i][j-1])*grid[i][j]
        return maximum[-1][-1]%(int(1e9+7)) if maximum[-1][-1]>-1 else -1
                    
        # if arr[i][j]>0 not change
        # else maximum minimum is changed 