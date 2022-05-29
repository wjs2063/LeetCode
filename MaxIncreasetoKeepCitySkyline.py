class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        #north,south is same
        ns=[]
        #west,east is same
        we=[]
        # nxn matrix
        row=len(grid)
        col=row
        # 2<=n<=50 n^2 is safe
        for matrix in grid:
            we.append(max(matrix))
        origin_sum=0
        for c in range(col):
            x=grid[0][c]
            for r in range(row):
                x=max(x,grid[r][c])
                origin_sum+=grid[r][c]
            ns.append(x)
        # now caculate skyline
        new_sum=0
        for i in range(row):
            for j in range(col):
                grid[i][j]=min(ns[j],we[i])
                new_sum+=grid[i][j]
        return new_sum-origin_sum
 
