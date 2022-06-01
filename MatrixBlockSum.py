class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m=len(mat)#row
        n=len(mat[0])#col
        prefix_sum=[[0]*(n+1) for _ in range(m+1)]
        answer=[[0]*n for _ in range(m)]
        val=0
        for i in range(m):
            for j in range(n):
                prefix_sum[i+1][j+1]=prefix_sum[i][j+1]+prefix_sum[i+1][j]-prefix_sum[i][j]+mat[i][j]
        for i in range(m):
            for j in range(n):
                r1=max(0,i-k)
                r2=min(m,i+k+1)
                l1=max(0,j-k)
                l2=min(n,j+k+1)
                answer[i][j]=prefix_sum[r2][l2]-prefix_sum[r2][l1]-prefix_sum[r1][l2]+prefix_sum[r1][l1]
        return answer
                